import csv
from itertools import islice
import json
import re
from dotenv import load_dotenv
import os
import uuid
import github
from tree_sitter import Parser
from tree_sitter_languages import get_language
import detect_language
import remove_comments
from comment_extractor import extract_comments_and_code_pairs, extract_from_content
from datetime import datetime
import time
import difflib
from github.InputGitTreeElement import InputGitTreeElement
from sentence_transformers import CrossEncoder

load_dotenv()

# GitHub repository details
GITHUB_OWNER = "BrandtBoys"  # Change this
REPO_NAME = "flask-fork"  # Change this
WORKFLOW_NAME = "update_docs.yml"  # Change if different
GITHUB_TOKEN = os.getenv("GITHUB_PAT")  # Use a Personal Access Token

# Generate a unique branch name
branch_name = f"test-agent-{uuid.uuid4()}"
#instantiate github auth
g = github.Github(login_or_token=GITHUB_TOKEN)
print("github")

#get repo
repo = g.get_repo(f"{GITHUB_OWNER}/{REPO_NAME}")
print("repo")

# Commits to compare (replace or allow user input)
start = 40  # what index of commit the test should start from
end =30  # what index of commit the test should end at

#set of files which have been modified during the test
modified_filepaths = set()

#the list of all commits from a given branch, where index 0 is HEAD
# commits = list(repo.get_commits(sha="main"))[end:start+1]
commits = list(islice(repo.get_commits(sha="main"), end, start))
print("commits")

#Branch out to test env, from the specified commit you want to start the test from
repo.create_git_ref(ref='refs/heads/' + branch_name, sha=commits[-1].sha)
print("create branch")
branch = repo.get_branch(branch_name)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Define the base results directory
os.makedirs("results", exist_ok=True)
result_file = os.path.join("results", f"{timestamp}.csv")
with open(result_file, mode="w", newline="", encoding="utf-8") as f:
    header = ["Semantic-Score", "Code", "Original-Comment","Agent-Comment", "Filename", "Agent-Commit"]
    writer = csv.writer(f)
    writer.writerow(header)

def main():

    #read the content of the agent, and add it into the test environment
    with open ("agent.py", "r") as f:
        agent_code = f.read()
        update_file("agent.py", agent_code)

    #Make a requirements file for th dependencies the workflow needs
    with open ("workflow_requirements.txt", "r") as f:
        workflow_requirements = f.read()
        update_file("workflow_requirements.txt", workflow_requirements)

    #read content of the workflow, and add it into the test environment
    with open (".github/workflows/update_docs.yml","r") as f:
        workflow_code = f.read()
        update_file(".github/workflows/update_docs.yml",workflow_code)
    
    #add loop of commits
    for commit in reversed(commits):
        print(commit)
        add_commit_run_agent(commit.sha)
    

def add_commit_run_agent(commit_sha):
    branch = repo.get_branch(branch_name)
    ref = repo.get_git_ref(f'heads/{branch_name}')
    #Get the HEAD commit of test branch
    head_commit_sha = branch.commit.sha 
    head_commit = repo.get_git_commit(head_commit_sha)
    #code diff between the HEAD commit and the next commit
    diff = repo.compare(head_commit_sha,commit_sha) 

    modified_files = []

    for file in diff.files:
        #This is to fix the meta problem of handling commits that changes update_docs
        if file.filename == ".github/workflows/update_docs.yml":
            continue
        #use helper script to detect which language the modified file is written in
        file_language = detect_language.detect_language(file.filename) 
        if not file_language:
            continue
        #add the file to the set of modified files:
        modified_filepaths.add(file.filename)

        #Get the version of the modified file from the new commit
        content = repo.get_contents(file.filename,ref=commit_sha).decoded_content
        #use helper script to remove all comments from the modified file
        cleaned_source = remove_comments.remove_comments(file_language,content).decode("utf-8")
        #get the content of the file from the current HEAD commit
        try:
            # Try to fetch the file from the current HEAD (test branch)
            head_content = repo.get_contents(file.filename,ref=head_commit_sha).decoded_content.decode("utf-8")
        except github.GithubException as e:
            if e.status == 404:
                print(f"File {file.filename} does not exist in {head_commit_sha} - treating as newly added file.")
                head_content = ""
            else:
                print(e.message)

        #compare the cleaned source with head, to figure out which comments in HEAD the new commit 
        #would remove, since the new commit holds no comments.
        differ = difflib.ndiff(head_content.splitlines(keepends=True), cleaned_source.splitlines(keepends=True))
        #change the generator object to a list
        differ_list = list(differ)
        #the new file, with the latest code changes, but the comments from the previous state.
        modified_differ = []
        for line in differ_list:
            if re.match(r"-\s*#", line):
                modified_differ.append(line[2:])
            else:
                modified_differ.append(line)

        modified_file = difflib.restore(modified_differ, 2)
        modified_file_str = "".join(modified_file)
        
        #add modified files to list
        modified_files.append((file.filename, modified_file_str))

    if commit_multiple_files(ref, modified_files, head_commit, "Add incoming files, replicated commit without comments."):
        workflow = repo.get_workflow(WORKFLOW_NAME)
        workflow.create_dispatch(ref=branch_name)
        time.sleep(5)

        # wait to see when the action is finished, before moving on.
        run = workflow.get_runs()[0]
        while run.status not in ["completed"]:
            print(f"Workflow running... (current status: {run.status})")
            time.sleep(5)  # Wait and check again
            run = workflow.get_runs()[0]  # Refresh latest run

    #fetch the latest changes to the test branch
    branch = repo.get_branch(branch_name)
    #fetch the HEAD commit of test branch
    agent_HEAD_commit = branch.commit.sha

    result_rows = []
    comment_pairs = []
    comment_metedata = []

    for filename, content in modified_files:
        file_language = detect_language.detect_language(filename) 
        if not file_language:
            continue
        original_content = repo.get_contents(filename,ref=commit_sha)
        original_comment_code_pairs = extract_from_content(original_content, file_language)

        agent_comment_code_pairs = get_agent_diff_content(repo, filename, agent_HEAD_commit, file_language)

        for agComment, agCode in agent_comment_code_pairs:
            for orgComment, orgCode in original_comment_code_pairs:
                if orgCode.strip() == agCode.strip() and orgComment.strip() != agComment.strip():
                    comment_pairs.append([orgComment, agComment])
                    comment_metedata.append([orgCode, filename, agent_HEAD_commit])

    if not comment_pairs:
        return

    scores = calculate_semantic_scores(comment_pairs)

    for score, (orgComment, agComment), (code, filename, commit) in zip(scores, comment_pairs, comment_metedata):
        result_rows.append([score, code, orgComment, agComment, filename, commit])

    with open(result_file, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(result_rows)

    

def commit_multiple_files(ref, files, last_commit, commit_message):
    if not files:
        print("No file-changes to commit")
        return False
    # Create blobs for each file (this uploads the content to GitHub)
    blobs = []
    for path, content in files:
        blob = repo.create_git_blob(content, "utf-8")
        blobs.append((path, blob))

    # Create a tree that includes all files
    tree_elements = []
    for path, blob in blobs:
        tree_element = InputGitTreeElement(path=path, mode="100644", type="blob", sha=blob.sha)
        tree_elements.append(tree_element)

    new_tree = repo.create_git_tree(tree_elements, last_commit.tree)

    new_commit = repo.create_git_commit(commit_message, new_tree, [last_commit])

    #Move the branch pointer to the new commit
    ref.edit(new_commit.sha)
    return True

def update_file(file_name, content):
    try:
        # Check if file exists in the branch
        contents = repo.get_contents(file_name, ref=branch_name)
        
        # If file exists, update it
        repo.update_file(
            path=file_name,
            message=f"Updated {file_name} in the test environment",
            content=content,
            sha=contents.sha,  # Required for updating an existing file
            branch=branch_name
        )

    except Exception as e:
        # If file doesn't exist, create it
        if "404" in str(e):  # File not found error
            repo.create_file(
                path=file_name,
                message=f"Added {file_name} to the test environment",
                content=content,
                branch=branch_name
            )
        else:
            raise  # Raise other unexpected errors

def calculate_semantic_scores(commentPairs):
    model = CrossEncoder("cross-encoder/stsb-roberta-base")
    scores = model.predict(commentPairs)
    return scores

def get_agent_diff_content(repo, filename, commit_sha, file_language):
    # Get commits and file contents
    commit = repo.get_commit(sha=commit_sha)
    old_content = repo.get_contents(filename, ref=commit.parents[0].sha).decoded_content.decode()
    new_content = repo.get_contents(filename, ref=commit.sha).decoded_content.decode()


    # Generate diff
    diff = difflib.unified_diff(
        old_content.splitlines(), new_content.splitlines(), n=0
    )

    # Extract changed line numbers
    changed_lines = set()
    for line in diff:
        if line.startswith("@@"):
            parts = line.split(" ")
            new_range = parts[2]  # like +12,3
            start_line = int(new_range.split(",")[0][1:])
            line_count = int(new_range.split(",")[1]) if "," in new_range else 1
            for i in range(start_line, start_line + line_count):
                changed_lines.add(i)

    # Tree-sitter parsing
    parser = Parser()
    language = get_language(file_language)
    parser.set_language(language)
    tree = parser.parse(bytes(new_content, "utf8"))
    root_node = tree.root_node

    # Find affected code blocks
    comments = []
    comment_code_pairs = []
    def find_comment_code_pairs(node, changed_lines):
        nonlocal comments, comment_code_pairs
        if node.type in ["comment", "block_comment"]:
            start_line = node.start_point[0] + 1
            end_line = node.end_point[0] + 1
            if any(line in changed_lines for line in range(start_line, end_line + 1)):
                comment_text = new_content[node.start_byte:node.end_byte].strip()
                # If the last comment is right above the current one, merge them
                if comments and comments[-1][1] == node.start_byte - 1:
                    comments[-1] = (comments[-1][0] + "\n" + comment_text, comments[-1][1])
                else:
                    comments.append((comment_text, node.start_byte))
        elif node.type in ["function_definition", "class_definition", "expression_statement", "assignment"]:
            code_text = new_content[node.start_byte:node.end_byte].strip()
            
            if comments:
                combined_comment = "\n".join(c[0] for c in comments)
                clean_code_text = remove_comments.remove_comments(file_language, code_text.encode("utf-8")).decode("utf-8")
                comment_code_pairs.append((combined_comment, clean_code_text))
                comments = []  # Reset comments after assignment
        for child in node.children:
            find_comment_code_pairs(child, changed_lines)
    find_comment_code_pairs(root_node, changed_lines)

    # Flatten blocks into strings

    with open("test.md", mode="w", encoding="utf-8") as f:
        f.write("## Old Content")
        f.write(old_content)
        f.write("## New Content")
        f.write(new_content)
        f.write("## Pruned")
        for comment, code in comment_code_pairs:
            f.write(f"Code: {code}, Comment: {comment}")
    
    return comment_code_pairs



if __name__ == "__main__":
    main()