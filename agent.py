from uuid import uuid4
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import git
import os

#create branch
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
diff = repo.git.diff("HEAD~1","HEAD","src/")
# print(diff)
diff_files = list(hcommit.diff("HEAD~1"))
source_path = str(diff_files[0].a_path)

# fetch docs files
with open(source_path, "r") as f:
    source_code = f.read()

# Create prompt for LLM
prompt = ChatPromptTemplate.from_template(
    """
    You are a documentation assistant. A code change was just committed.

    ## Instructions:
    - Only modify the provided `source_code` by adding inline comments at the end of lines that have been changed in `code_diff`.
    - Do not modify any other lines of `source_code`.
    - Do not add any headers, footers, explanations, or extra text.
    - Return the fully formatted `source_code` with the new inline comments added to the changed lines.

    ## Code Change:
    {code_diff}

    ## Previous Source Code:
    {source_code}

    Return the updated source code with inline comments added only to the changed lines:
    """
)

prompt_input = prompt.format(
    code_diff = diff,
    source_code = source_code
)

# the LLM does it work
llm = ChatOllama(model="llama3.2", temperature=0.1)
llm_response = llm.invoke(prompt_input)

# Write changes to docs
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