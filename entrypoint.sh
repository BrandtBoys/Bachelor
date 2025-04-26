#!/bin/sh -l

# Install Git
apt-get update
apt-get install -y git
apt-get install -y curl

# Tell the action to trust github/workspace - to avoid "dubious ownership"
git config --global --add safe.directory /github/workspace

# Login on git with DocTide bot
git config --global user.name "DocTide[bot]"
git config --global user.email "DocTide[bot]@users.noreply.github.com"
git remote set-url origin https://x-access-token:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}.git

# Install doctide.py dependencies
pip install -r workflow_requirements.txt

# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull Ollama model
ollama pull llama3.2

# Run Doctide agent
python agent.py

# Test mode:
if [ $1 ]
then
    # Checkout back to the caller test-branch
    git checkout "${GITHUB_REF#refs/heads/}"
    # Fetch the update-docs branch, the agent has just made
    git fetch origin $BRANCH_NAME # An env variable set by the agent script
    # Merge test-branch and update-docs branch
    git merge origin/$BRANCH_NAME
    # Delete the update-docs branch
    git push -d origin $BRANCH_NAME
    git push origin HEAD
else
    gh auth setup-git
    gh pr create -B main -H $BRANCH_NAME --fill-first
fi