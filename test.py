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
from github.InputGitTreeElement import InputGitTreeElement

load_dotenv()


GITHUB_OWNER = "BrandtBoys"  
REPO_NAME = "Bachelor"  
WORKFLOW_NAME = "update_docs.yml"  
GITHUB_TOKEN = os.getenv("GITHUB_PAT")  


branch_name = f"test-agent-{uuid.uuid4()}"


g = github.Github(login_or_token=GITHUB_TOKEN)


repo = g.get_repo(f"{GITHUB_OWNER}/{REPO_NAME}")


start = 3  
end = 0  


modified_filepaths = set()


commits = list(repo.get_commits(sha="main")) 


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
    
    for file in modified_filepaths:
      # make folder to store results in
        
        file_dir = os.path.join(results_dir, file)
        os.makedirs(file_dir, exist_ok=True)

        file_language = detect_language.detect_language(file)
        if not file_language:
            continue
        agent_content = repo.get_contents(file,ref=agent_HEAD_commit)
        agent_comment_code_pairs = extract_from_content(agent_content, file_language)

      # extract only the file name, not folders and format.
        
        file_name = re.sub(r".*/|\.py$", "", file)

      # Define JSON file path
        
        agent_json_file_path = os.path.join(file_dir, f"agent_{file_name}.json")

      # Save extracted data to JSON
        
        with open(agent_json_file_path, "w", encoding="utf-8") as f:
            json.dump(agent_comment_code_pairs, f, indent=4)

        original_content = repo.get_contents(file,ref=commits[0].sha)
        original_comment_code_pairs = extract_from_content(original_content, file_language)

        original_json_file_path = os.path.join(file_dir, f"original_{file_name}.json")

      # Save extracted data to JSON
        
        with open(original_json_file_path, "w", encoding="utf-8") as f:
            json.dump(original_comment_code_pairs, f, indent=4)



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
      #add the file to the set of modified files:
        
        file_language = detect_language.detect_language(file.filename) 
        if not file_language:
            continue
        
        modified_filepaths.add(file.filename)

        
      #use helper script to detect which language the modified file is written in
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

    commit_multiple_files(ref, modified_files, head_commit, "Add incoming files, replicated commit without comments.")
    workflow = repo.get_workflow(WORKFLOW_NAME)
    workflow.create_dispatch(ref=branch_name)
    time.sleep(5)

  # wait to see when the action is finished, before moving on.
    
    run = workflow.get_runs()[0]
    while run.status not in ["completed"]:
        print(f"Workflow running... (current status: {run.status})")
        time.sleep(5)  
        run = workflow.get_runs()[0]  

def commit_multiple_files(ref, files, last_commit, commit_message):
  # Create blobs for each file (this uploads the content to GitHub)
    if not files:
        print("No file-changes to commit")
        return
    
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

def update_file(file_name, content):
    try:
      # Check if file exists in the branch
        
        contents = repo.get_contents(file_name, ref=branch_name)
        
      # If file exists, update it
        
        repo.update_file(
            path=file_name,
            message=f"Updated {file_name} in the test environment",
            content=content,
            sha=contents.sha,  
            branch=branch_name
        )

    except Exception as e:
      # If file doesn't exist, create it
        
        if "404" in str(e):  
            repo.create_file(
                path=file_name,
                message=f"Added {file_name} to the test environment",
                content=content,
                branch=branch_name
            )
        else:
            raise  

if __name__ == "__main__":
    main()