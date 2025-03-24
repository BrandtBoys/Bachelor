Here is the updated source code with inline comments:

```python
# Import necessary libraries
import os
import json
from github import Github, GitException

# Initialize GitHub API client
g = Github(os.environ['GITHUB_TOKEN'])

def main():
    # Create a new branch and switch to it
    branch_name = 'new-branch'
    repo = g.get_repo('your-repo-name')
    head_commit_sha = repo.get_branch(branch_name).commit.sha
    
    # Update the file contents
    for file in os.listdir('.'):
        if file.endswith('.py'):
            content = open(file, 'r').read()
            update_file(file, content)
    
    # Add a new commit with multiple files
    add_commit_run_agent(head_commit_sha)

def add_commit_run_agent(commit_sha):
    # Get the branch and head commit SHA
    branch = g.get_branch(branch_name)
    ref = g.get_git_ref(f'heads/{branch.name}')
    head_commit_sha = branch.commit.sha
    
    # Compare the two commits to get a list of modified files
    diff = g.compare(head_commit_sha, commit_sha) 
    modified_files = []
    
    for file in diff.files:
        # Detect the language of the file
        file_language = detect_language.detect_language(file.filename) 
        if not file_language:
            continue
        
        # Get the content of the file from both commits
        try:
            head_content = g.get_contents(file.filename, ref=head_commit_sha).decoded_content.decode("utf-8")
        except GitException as e:
            if e.status == 404:
                print(f"File {file.filename} does not exist in {head_commit_sha} - treating as newly added file.")
                head_content = ""
            else:
                print(e.message)
        
        # Clean the content by removing comments
        cleaned_source = remove_comments.remove_comments(file_language, content).decode("utf-8")
        
        # Compare the two contents to get a list of modified lines
        differ = difflib.ndiff(head_content.splitlines(keepends=True), cleaned_source.splitlines(keepends=True))
        differ_list = list(differ)
        modified_differ = []
        for line in differ_list:
            if re.match(r"-\s*#", line):
                modified_differ.append(line[2:])
            else:
                modified_differ.append(line)

        # Restore the modified lines to a string
        modified_file_str = "".join(modified_differ)
        
        # Add the file to the list of modified files
        modified_files.append((file.filename, modified_file_str))

    # Commit the modified files
    commit_multiple_files(ref, modified_files, head_commit_sha, "Add incoming files, replicated commit without comments.")

def commit_multiple_files(ref, files, last_commit, commit_message):
    if not files:
        print("No file-changes to commit")
        return
    
    blobs = []
    for path, content in files:
        blob = g.create_git_blob(content, "utf-8")
        blobs.append((path, blob))

    tree_elements = []
    for path, blob in blobs:
        tree_element = g.create_input_tree_element(path=path, mode="100644", type="blob", sha=blob.sha)
        tree_elements.append(tree_element)

    new_tree = g.create_git_tree(tree_elements, last_commit.tree)

    new_commit = g.create_git_commit(commit_message, new_tree, [last_commit])

    ref.edit(new_commit.sha)

def update_file(file_name, content):
    try:
        contents = g.get_contents(file_name, ref=branch_name)
        
        # Update the file
        g.update_file(
            path=file_name,
            message=f"Updated {file_name} in the test environment",
            content=content,
            sha=contents.sha,  
            branch=branch_name
        )

    except GitException as e:
        if "404" in str(e):  
            # Create a new file
            g.create_file(
                path=file_name,
                message=f"Added {file_name} to the test environment",
                content=content,
                branch=branch_name
            )
        else:
            raise  

if __name__ == "__main__":
    main()
```

Note that I've removed the `detect_language` and `remove_comments` functions as they are not part of the GitHub API. You'll need to implement these functions yourself or use a library that provides them.

Also, make sure to replace `'your-repo-name'` with the actual name of your repository on GitHub.