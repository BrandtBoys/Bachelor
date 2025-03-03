from dotenv import load_dotenv
import requests
import os
import subprocess
import uuid
import github
import detect_language
import remove_comments

load_dotenv()

# GitHub repository details
GITHUB_OWNER = "BrandtBoys"  # Change this
REPO_NAME = "Bachelor"  # Change this
WORKFLOW_NAME = "update_docs.yml"  # Change if different
GITHUB_TOKEN = os.getenv("GITHUB_PAT")  # Use a Personal Access Token

# Commits to compare (replace or allow user input)
start_commit = "dbf0743"  # Example commit hash or HEAD~1
new_commits = "cececd9"  # One or more new commits

# Generate a unique branch name
branch_name = f"test-agent-{uuid.uuid4()}"

#instantiate github auth
g = github.Github(login_or_token=GITHUB_TOKEN)

#get repo
repo = g.get_repo(f"{GITHUB_OWNER}/{REPO_NAME}")


#Branch out to test env, from the specified commit you want to start the test from
repo.create_git_ref(ref='refs/heads/' + branch_name, sha=repo.get_commit(start_commit).sha)

#read the content of the agent
with open ("agent.py", "r") as f:
    agent_code = f.read()

#read content of the workflow
with open (".github/workflows/update_docs.yml","r") as f:
    workflow_code = f.read()
    
#add the content of the agent to the test branch
try:
    # Check if file exists in the branch
    contents = repo.get_contents("agent.py", ref=branch_name)
    
    # If file exists, update it
    repo.update_file(
        path="agent.py",
        message="Updated agent.py in the test environment",
        content=agent_code,
        sha=contents.sha,  # Required for updating an existing file
        branch=branch_name
    )

except Exception as e:
    # If file doesn't exist, create it
    if "404" in str(e):  # File not found error
        repo.create_file(
            path="agent.py",
            message="Added agent.py to the test environment",
            content=agent_code,
            branch=branch_name
        )
    else:
        raise  # Raise other unexpected errors

#add the content of the workflow to the test environment
try:
    # Check if file exists in the branch
    contents = repo.get_contents(".github/workflows/update_docs.yml", ref=branch_name)
    
    # If file exists, update it
    repo.update_file(
        path=".github/workflows/update_docs.yml",
        message="Updated workflow in the test environment",
        content=workflow_code,
        sha=contents.sha,  # Required for updating an existing file
        branch=branch_name
    )

except Exception as e:
    # If file doesn't exist, create it
    if "404" in str(e):  # File not found error
        repo.create_file(
            path=".github/workflows/update_docs.yml",
            message="Added workflow to the test environment",
            content=workflow_code,
            branch=branch_name
        )
    else:
        raise  # Raise other unexpected errors

#add loop ofg commits

#add new commits to the test branch.
diff = repo.compare(start_commit,new_commits)

for file in diff.files:
    file_language = detect_language.detect_language(file.filename)
    content = repo.get_contents(file.filename,ref=repo.get_commit(new_commits).sha).decoded_content
    cleaned_source = remove_comments.remove_comments(file_language,content).decode("utf-8")
    try:
        # Check if file exists in the branch
        contents = repo.get_contents(file.filename, ref=branch_name)
        
        # If file exists, update it
        repo.update_file(
            path=file.filename,
            message="Updated {file_path} in the test environment",
            content=cleaned_source,
            sha=contents.sha,  # Required for updating an existing file
            branch=branch_name
        )

    except Exception as e:
        # If file doesn't exist, create it
        if "404" in str(e):  # File not found error
            repo.create_file(
                path=file.filename,
                message="Added {file_path} to the test environment",
                content=cleaned_source,
                branch=branch_name
            )
        else:
            raise  # Raise other unexpected errors
