import csv
from itertools import islice
from dotenv import load_dotenv
from dt_diff_lib import extract_data, collect_comment_range
import os
import uuid
import github #pyGithub
import detect_language
from datetime import datetime
import time
from github.InputGitTreeElement import InputGitTreeElement
from metrics import create_csv

load_dotenv()

counter = 0

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
start = 36  # what index of commit the test should start from, have to be higher than "end"
end = 34  # what index of commit the test should end at

#set of files which have been modified during the test
modified_filepaths = set()

#the list of all commits from a given branch, where index 0 is HEAD
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

    with open ("detect_language.py", "r") as f:
        detect_language_code = f.read()
        update_file("detect_language.py", detect_language_code)
    
    with open ("dt_diff_lib.py", "r") as f:
        dt_diff_lib_code = f.read()
        update_file("dt_diff_lib.py", dt_diff_lib_code)

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
        head_content = ""
        try:
            head_content = repo.get_contents(file.filename, ref= head_commit_sha).decoded_content.decode("utf-8")
        except Exception:
            print("file does not exist")
        #use helper script to remove all comments from the modified file
        cleaned_commit = remove_diff_comments(file_language, head_content, content.decode("utf-8"))
        
        #add modified files to list
        modified_files.append((file.filename, cleaned_commit))

    if commit_multiple_files(ref, modified_files, head_commit, "Add incoming files, replicated commit without comments."):
        workflow = repo.get_workflow(WORKFLOW_NAME)
        workflow.create_dispatch(ref=branch_name)
        time.sleep(5)

        # wait to see when the action is finished, before moving on.
        run = workflow.get_runs()[0]
        while run.status not in ["completed"]:
            time.sleep(5)  # Wait and check again
            run = workflow.get_runs()[0]  # Refresh latest run

    create_csv(repo, branch_name, modified_files, commit_sha, result_file)

    

def commit_multiple_files(ref, files, last_commit, commit_message):
    """
    Commit multiple files to a GitHub branch using the PyGithub API.

    This function stages and commits multiple file changes in a single Git commit,
    then moves the specified branch reference to the new commit.

    Parameters
    ----------
    ref : github.Reference
        The reference object for the branch (e.g., `repo.get_git_ref("heads/main")`).
    files : list of tuple[str, str]
        A list of tuples where each tuple contains:
        - path (str): the file path in the repo.
        - content (str): the file content to commit.
    last_commit : github.GitCommit
        The last commit object on the branch, used as the parent for the new commit.
    commit_message : str
        The commit message for the new commit.

    Returns
    -------
    bool
        True if the commit was created and the branch pointer was updated.
        False if there were no files to commit.

    Notes
    -----
    - This function assumes access to a global `repo` object (of type `github.Repository.Repository`).
    - Uses UTF-8 encoding for file content.
    """
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
    """
    Update or create a file in a GitHub repository branch using the PyGithub API.

    This function checks if the specified file exists in a branch (`branch_name`). If it exists,
    the file is updated with new content. If it does not exist (404 error), the file is created.

    Parameters
    ----------
    file_name : str
        The name (or path) of the file to update or create in the repository.
    content : str
        The new content to write to the file.

    Raises
    ------
    Exception
        If an unexpected error occurs during the GitHub API call (excluding 404).
    """
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

def remove_diff_comments(file_language, head_content, commit_content):
    """
    Remove comments from functions that were changed in a commit diff.

    This function uses Tree-sitter to identify comments within function definitions that are
    affected by a code diff (between `head_content` and `commit_content`). It then removes
    those specific comment byte ranges from the `commit_content`.

    Parameters
    ----------
    file_language : str
        The programming language of the file (e.g., "python", "javascript") used to initialize the Tree-sitter parser.
    head_content : str
        The content of the file in the base (head) revision, used for diff comparison.
    commit_content : str
        The content of the file in the new (commit) revision, from which comments will be removed.

    Returns
    -------
    str
        The updated source code with targeted diff-related comments removed.
    """
    global counter
    counter += 1
    # Extract comment ranges
    diff_comments_byte_range = extract_data(True, file_language, head_content, commit_content, collect_comment_range)
    cleaned_code = bytearray(commit_content.encode("utf-8"))
    if diff_comments_byte_range:
        for start_byte, end_byte in reversed(diff_comments_byte_range):
            cleaned_code[start_byte:end_byte] = b""
    print("No comment found")
    
    return(cleaned_code.decode("utf-8"))



if __name__ == "__main__":
    main()