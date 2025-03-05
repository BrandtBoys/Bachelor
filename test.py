from dotenv import load_dotenv
import os
import uuid
import github
import detect_language
import remove_comments
import time

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
start = 2  # what index of commit the test should start from
end = 0  # what index of commit the test should end at

commits = list(repo.get_commits(sha="main")) #the list of all commits from a given branch, where index 0 is HEAD

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
    for commit in reversed(commits[start:end-1:-1]):
        add_commit_run_agent(commit.sha)
    

def add_commit_run_agent(commit_sha):
    #add new commits to the test branch.
    head_commit = branch.commit.sha #The HEAD of test branch
    diff = repo.compare(head_commit,commit_sha) #code diff between the HEAD commit and the next commit

    for file in diff.files:
        file_language = detect_language.detect_language(file.filename)
        content = repo.get_contents(file.filename,ref=commit_sha).decoded_content
        cleaned_source = remove_comments.remove_comments(file_language,content).decode("utf-8")
        update_file(file.filename, cleaned_source)

    workflow = repo.get_workflow(WORKFLOW_NAME)
    workflow.create_dispatch(ref=branch_name)

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