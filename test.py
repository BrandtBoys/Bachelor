Here is a refactored version of your code, following best practices and readability guidelines:

```python
import os
import time
from github import Github, GitException

# GitHub API credentials
g = Github(os.environ['GITHUB_TOKEN'])

def detect_language(file_name):
    """Detects the language of a file"""
    # Implement your own logic to detect the language
    # For simplicity, let's assume we have a function called `detect_language` in another module
    from your_module import detect_language
    return detect_language(file_name)

def remove_comments(content, language):
    """Removes comments from a file content"""
    # Implement your own logic to remove comments
    # For simplicity, let's assume we have a function called `remove_comments` in another module
    from your_module import remove_comments
    return remove_comments(content, language)

def compare_files(head_commit_sha, commit_sha):
    """Compares two files and returns the modified content"""
    try:
        head_content = g.git.show(f'{head_commit_sha}:{commit_sha}')
    except GitException as e:
        if e.status == 404:
            print(f"File {commit_sha} does not exist in {head_commit_sha}")
            return "", ""
        else:
            raise

    try:
        commit_content = g.git.show(f'{commit_sha}:{commit_sha}')
    except GitException as e:
        if e.status == 404:
            print(f"File {commit_sha} does not exist")
            return "", ""
        else:
            raise

    differ = difflib.ndiff(head_content.splitlines(keepends=True), commit_content.splitlines(keepends=True))
    modified_differ = []
    for line in differ:
        if re.match(r"- \s*#", line):
            modified_differ.append(line[2:])
        else:
            modified_differ.append(line)

    return difflib.restore(modified_differ, 2), ""

def add_commit_run_agent(commit_sha, branch_name):
    """Adds a new commit to the repository and runs the workflow"""
    try:
        head_commit = g.git.show(f'{branch_name}:HEAD')
    except GitException as e:
        if e.status == 404:
            print("Branch does not exist")
            return
        else:
            raise

    diff = g.git.compare(head_commit, commit_sha)

    modified_files = []
    for file in diff.files:
        file_language = detect_language(file.filename)
        if file_language:
            try:
                head_content = g.git.show(f'{branch_name}:HEAD:{file.filename}')
            except GitException as e:
                if e.status == 404:
                    print(f"File {file.filename} does not exist in {branch_name}")
                    continue
                else:
                    raise

            commit_content = g.git.show(f'{commit_sha}:{file.filename}')

            modified_content, _ = compare_files(head_commit, commit_sha)

            cleaned_source = remove_comments(commit_content, file_language)
            if head_content != cleaned_source:
                print(f"Modified {file.filename} with new content")

            modified_file = difflib.restore(modified_differ, 2)
            modified_file_str = "".join(modified_file)

            modified_files.append((file.filename, modified_file_str))

    commit_multiple_files(branch_name, modified_files, g.git.show(f'{branch_name}:HEAD'), "Add incoming files, replicated commit without comments")

def update_file(file_name, content):
    """Updates a file in the repository"""
    try:
        contents = g.git.show(f'{file_name}', ref=branch_name)
    except GitException as e:
        if e.status == 404:
            print(f"File {file_name} does not exist")
            return
        else:
            raise

    g.git.update_file(file_name, message=f"Updated {file_name} in the test environment", content=content, sha=contents.sha)

def main():
    branch_name = "main"
    commit_sha = "HEAD"

    add_commit_run_agent(commit_sha, branch_name)
    update_file("your_file.py", "Your updated file content")

if __name__ == "__main__":
    main()
```

Note that I've made the following changes:

*   Reorganized the code into smaller functions with clear responsibilities.
*   Removed redundant comments and improved code readability.
*   Used more descriptive variable names to make the code easier to understand.
*   Added error handling for cases where files do not exist or cannot be updated.
*   Improved the organization of the code by grouping related functions together.

This refactored version should be more maintainable, efficient, and readable. However, please note that you may need to adjust it according to your specific requirements and GitHub API usage.