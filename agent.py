import sys
from uuid import uuid4
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import git
import os

# Get arguments or set defaults
print("before new stuff")
current_commit = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] else "HEAD~1"
new_commit = sys.argv[2] if len(sys.argv) > 2 and sys.argv[2] else "HEAD"

#create branch
print("after new stuff")
repo = git.Repo(".")
branch_id = uuid4()
branch_name = "Update-docs-" + str(branch_id)
repo.git.branch(branch_name)
repo.git.checkout(branch_name)

# Set the branch name in the GitHub Actions environment
with open(os.getenv('GITHUB_ENV'), "a") as env_file:
    env_file.write(f"BRANCH_NAME={branch_name}\n")

# Compare changes and create diff
hcommit = repo.head.commit
diff = repo.git.diff(current_commit, new_commit,"src/")
# print(diff)
diff_files = list(hcommit.diff("HEAD~1"))
source_path = str(diff_files[0].a_path)

# fetch docs files
print("Reading files")
with open(source_path, "r") as f:
    source_code = f.read()

# Create prompt for LLM
prompt = ChatPromptTemplate.from_template(
    """
    You are a documentation assistant. A code change was just committed.

    ## Instructions:
    - Only modify the provided `source_code` by adding inline comments to explain the functionality of the code.
    - Focus on the lines changed in `code_diff`, but you may look a few lines above and below the changes to understand their context.
    - Do **not** modify any code. Only add comments.
    - The comments should explain **why** the code works the way it does, not just describe what was changed.
    - Ensure the comments are clear, concise, and helpful.
    - Do **not** add headers, footers, explanations, or any extra text. Only return the fully formatted `source_code` with comments added.

    ## Code Change:
    {code_diff}

    ## Previous Source Code:
    {source_code}

    Return the updated source code with inline comments that explain the changed functionality:
    """
)

prompt_input = prompt.format(
    code_diff = diff,
    source_code = source_code
)

# the LLM does it work
print("Initializing LLM")
llm = ChatOllama(model="deepseek-r1:8b", temperature=0.1)
print("Invoking LLM")
llm_response = llm.invoke(prompt_input)

# Write changes to docs
print("Writing changes to file")
with open(source_path, "w") as f:
    f.write(llm_response.content)

# Add changes
add_files = [source_path]
repo.index.add(add_files)

# Commit changes
repo.index.commit("Updated inline documentation")

# Push changes
# try:
#     repo.create_remote("origin", url="git@github.com:BrandtBoyz/Bachelor")
# except git.exc.GitCommandError as e:
#     print(f"error: {e}")

repo.remotes.origin.push(refspec=f"{branch_name}:{branch_name}",set_upstream=True)

repo.__del__()
exit(0)