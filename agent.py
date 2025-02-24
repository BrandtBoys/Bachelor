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

# Compare changes and create diff
hcommit = repo.head.commit
diff = repo.git.diff("HEAD~1","HEAD","src/")
# print(diff)
diff_files = hcommit.diff("HEAD~1")
source_path = str(diff_files[0])

# fetch docs files
with open(source_path, "r") as f:
    source_code = f.read()

# Create prompt for LLM
prompt = ChatPromptTemplate.from_template(
    """
    You are a documentation assistant. A code change was just committed.

    ## Code Change:
    {code_diff}

    ## Previous source code:
    {source_code}

    Update the inline-documentation to reflect the code change. The only way you shall change the source code is by adding inline documentation. You should return the entire source code with the inline documentation added.
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