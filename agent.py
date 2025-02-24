from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import git
import os

#create branch
repo = git.Repo(".")
branch_name = "Update-docs"
repo.git.branch(branch_name)
repo.git.checkout(branch_name)

# Compare changes and create diff
hcommit = repo.head.commit
diff_files = hcommit.diff("HEAD~1").iter_change_type("M")
for f in diff_files:
    print(f)
diff = repo.git.diff("HEAD~1","HEAD","src/")
print(diff)

# fetch source code
path = str(diff_files[0])
with open(path, "r") as f:
    source_code = f.read()

# Create prompt for LLM
prompt = ChatPromptTemplate.from_template(
    """
    You are a documentation assistant. A code change was just committed.

    ## Code Change:
    {code_diff}

    ## Source file:
    {source_code}

    Update the inline- documentation to reflect the code change. Do not change anything in the source file besides adding inline comments.
    You should return the entire source-code now with your added inline documentation.
    """
)

prompt_input = prompt.format(
    code_diff = diff,
    source_code = source_code
)

# # the LLM does it work
llm = ChatOllama(model="llama3.2", temperature=0.1)
llm_response = llm.invoke(prompt_input)

# # Write changes to docs
with open(path, "w") as f:
    f.write(llm_response.content)

# # Add changes
add_files = [path]
repo.index.add(add_files)

# # Commit changes
repo.index.commit("Updated docs files")

# Push changes
# try:
#     repo.create_remote("origin", url="git@github.com:BrandtBoyz/Bachelor")
# except git.exc.GitCommandError as e:
#     print(f"error: {e}")

repo.remotes.origin.push(refspec=f"{branch_name}:{branch_name}",set_upstream=True)

repo.__del__()
exit(0)