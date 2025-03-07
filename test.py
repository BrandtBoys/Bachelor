import json
import re
from dotenv import load_dotenv
import os
import uuid
import github
import detect_language
import remove_comments
from comment_extractor import extract_from_content
from datetime import datetime
import time
import difflib

load_dotenv()

# GitHub repository details
GITHUB_OWNER = "BrandtBoys"  # Change this
REPO_NAME = "Bachelor"  # Change this
WORKFLOW_NAME = "update_docs.yml"  # Change if different
GITHUB_TOKEN = os.getenv("GITHUB_PAT")  # Use a Personal Access Token

# Generate a unique branch name
branch_name = f"test-agent-{uuid.uuid4()}"

#instantiate github auth
g = github.Github(login_or_token=GITHUB_TOKEN)

#get repo
repo = g.get_repo(f"{GITHUB_OWNER}/{REPO_NAME}")

# Commits to compare (replace or allow user input)
start = 3  # what index of commit the test should start from
end = 1  # what index of commit the test should end at

#set of files which have been modified during the test
modified_files = set()

#the list of all commits from a given branch, where index 0 is HEAD
commits = list(repo.get_commits(sha="main")) 

#Branch out to test env, from the specified commit you want to start the test from
repo.create_git_ref(ref='refs/heads/' + branch_name, sha=commits[start].sha)
branch = repo.get_branch(branch_name)

def main():

    #read the content of the agent, and add it into the test environment
    with open ("agent.py", "r") as f:
        agent_code = f.read()
        update_file("agent.py", agent_code)

    #read content of the workflow, and add it into the test environment
    with open (".github/workflows/update_docs.yml","r") as f:
        workflow_code = f.read()
        update_file(".github/workflows/update_docs.yml",workflow_code)
    
    #add loop of commits
    for commit in reversed(commits[end:start]):
        print(commit)
        add_commit_run_agent(commit.sha)
    
    #fetch the latest changes to the test branch
    branch = repo.get_branch(branch_name)
    #fetch the HEAD commit of test branch
    agent_HEAD_commit = branch.commit.sha

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Define the base results directory
    results_dir = os.path.join("results", timestamp)
    os.makedirs(results_dir, exist_ok=True)

    #given source code, pairs of code and their associated comments are saved in list
    for file in modified_files:
        # make folder to store results in
        file_dir = os.path.join(results_dir, file)
        os.makedirs(file_dir, exist_ok=True)

        file_language = detect_language.detect_language(file) 

        agent_content = repo.get_contents(file,ref=agent_HEAD_commit)
        agent_comment_code_pairs = extract_from_content(agent_content, file_language)

        # extract only the file name, not folders and format.
        file_name = re.sub(r".*/|\.py$", "", file)

        # Define JSON file path
        agent_json_file_path = os.path.join(file_dir, f"agent_{file_name}.json")

        # Save extracted data to JSON
        with open(agent_json_file_path, "w", encoding="utf-8") as f:
            json.dump(agent_comment_code_pairs, f, indent=4)

        original_content = repo.get_contents(file,ref=commits[0])
        original_comment_code_pairs = extract_from_content(original_content, file_language)

        original_json_file_path = os.path.join(file_dir, f"original_{file_name}.json")

        # Save extracted data to JSON
        with open(original_json_file_path, "w", encoding="utf-8") as f:
            json.dump(original_comment_code_pairs, f, indent=4)



def add_commit_run_agent(commit_sha):
    branch = repo.get_branch(branch_name)
    #Get the HEAD commit of test branch
    head_commit = branch.commit.sha 
    print(head_commit)
    #code diff between the HEAD commit and the next commit
    diff = repo.compare(head_commit,commit_sha) 

    for file in diff.files:
        #add the file to the set of modified files:
        modified_files.add(file.filename)
        #use helper script to detect which language the modified file is written in
        file_language = detect_language.detect_language(file.filename) 
        #Get the version of the modified file from the new commit
        content = repo.get_contents(file.filename,ref=commit_sha).decoded_content
        #use helper script to remove all comments from the modified file
        cleaned_source = remove_comments.remove_comments(file_language,content).decode("utf-8")
        #get the content of the file from the current HEAD commit
        head_content = repo.get_contents(file.filename,ref=head_commit).decoded_content.decode("utf-8")
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
        
        #commit the modified file to the branch
        update_file(file.filename,modified_file_str)


    workflow = repo.get_workflow(WORKFLOW_NAME)
    workflow.create_dispatch(ref=branch_name)
    time.sleep(5)

    # wait to see when the action is finished, before moving on.
    run = workflow.get_runs()[0]
    while run.status not in ["completed"]:
        print(f"Workflow running... (current status: {run.status})")
        time.sleep(5)  # Wait and check again
        run = workflow.get_runs()[0]  # Refresh latest run

def update_file(file_name, content):
    try:
        # Check if file exists in the branch
        contents = repo.get_contents(file_name, ref=branch_name)
        
        # If file exists, update it
        repo.update_file(
            path=file_name,
            message="Updated ${file_name} in the test environment",
            content=content,
            sha=contents.sha,  # Required for updating an existing file
            branch=branch_name
        )

    except Exception as e:
        # If file doesn't exist, create it
        if "404" in str(e):  # File not found error
            repo.create_file(
                path=file_name,
                message="Added ${file_name} to the test environment",
                content=content,
                branch=branch_name
            )
        else:
            raise  # Raise other unexpected errors

if __name__ == "__main__":
    main()