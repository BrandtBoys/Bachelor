from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import git
import os

#create branch
repo = git.Repo("../.")
branch_name = "Update-docs"
repo.git.branch(branch_name)
repo.git.checkout(branch_name)

# fetch docs files
docs_path = "docs/software_docs.md"
with open(docs_path, "r") as f:
    current_docs = f.read()

# Compare changes and create diff
hcommit = repo.head.commit
diff = repo.git.diff("HEAD~1","HEAD","mvp/src/")
print(diff)

# Create prompt for LLM
prompt = ChatPromptTemplate.from_template(
    """
    You are a documentation assistant. A code change was just committed.

    ## Code Change:
    {code_diff}

    ## Current Documentation:
    {prev_docs}

    Update the documentation to reflect the code change.
    """
)

prompt_input = prompt.format(
    code_diff = diff,
    prev_docs = current_docs
)

# the LLM does it work
llm = ChatOllama(model="llama3.2", temperature=0.1)
llm_response = llm.invoke(prompt_input)

# Write changes to docs
with open(docs_path, "w") as f:
    f.write(llm_response.content)

# Add changes
add_files = ["mvp/docs/software_docs.md"]
repo.index.add(add_files)

# Commit changes
repo.index.commit("Updated docs files")

# Push changes
# try:
#     repo.create_remote("origin", url="git@github.com:BrandtBoyz/Bachelor")
# except git.exc.GitCommandError as e:
#     print(f"error: {e}")

repo.remotes.origin.push(set_upstream=True)

repo.__del__()
exit(0)