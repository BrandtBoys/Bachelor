from dotenv import load_dotenv
import requests
import os
import subprocess
import uuid
import github

load_dotenv()

# GitHub repository details
GITHUB_OWNER = "BrandtBoys"  # Change this
REPO_NAME = "Bachelor"  # Change this
WORKFLOW_NAME = "update-docs.yml"  # Change if different
GITHUB_TOKEN = os.getenv("GITHUB_PAT")  # Use a Personal Access Token

# Commits to compare (replace or allow user input)
current_commit = "dbf0743"  # Example commit hash or HEAD~1
new_commit = "cececd9"  # Example commit hash or HEAD

# Generate a unique branch name
branch_name = f"test-update-docs-{uuid.uuid4().hex[:8]}"

try:
    # Clone the repo (or use existing local repo)
    g = github.Github(login_or_token=os.environ["GITHUB_PAT"])

    repo = g.get_repo(f"{GITHUB_OWNER}/{REPO_NAME}")

    subprocess.run(["git", "fetch", "origin"], check=True)

    # Create and checkout the new branch from current_commit
    print(f"🔀 Creating new branch '{branch_name}' from {current_commit}...")
    subprocess.run(["git", "checkout", "-b", branch_name, current_commit], check=True)

    # Push the branch to GitHub
    print(f"📤 Pushing branch '{branch_name}' to GitHub...")
    subprocess.run(["git", "push", "-u", "origin", branch_name], check=True)

    # GitHub API URL to trigger workflow
    workflow = repo.get_workflow(WORKFLOW_NAME)
    # url = f"https://api.github.com/repos/{GITHUB_OWNER}/{REPO_NAME}/actions/workflows/{WORKFLOW_NAME}/dispatches"

    # API request payload
    payload = {
        "ref": branch_name,  # Run workflow on this new branch
        "inputs": {
            "currentCommit": "HEAD",
            "newCommit": new_commit,
            "branch_name": branch_name
        }
    }

    # Headers for authentication
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"Bearer {GITHUB_TOKEN}"
    }

    # Trigger the workflow
    workflow.create_dispatch(ref=branch_name)
    # response = requests.post(url, json=payload, headers=headers)
except github.GithubException as e:
    print(f"❌ GitHub API Error: {e.status} - {e.data}")
    exit(1)
except Exception as e:
    print(f"❌ Unexpected Error: {e}")
    exit(1)
# Check response
# if response.status_code == 204:
#     print(f"✅ Workflow '{WORKFLOW_NAME}' triggered successfully on branch '{branch_name}'!")
# else:
#     print(f"❌ Failed to trigger workflow. Response: {response.text}")
