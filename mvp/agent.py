from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import git
import gc
from difflib import Differ
from pprint import pprint

docs_path = "docs/software_docs.md"
with open(docs_path, "r") as f:
    current_docs = f.read()

# # repo = git.Repo(".")
# diff = """diff --git a/src/main.py b/src/main.py
# index 3f8b2c4..1a2b3d5 100644
# --- a/main.py
# +++ b/main.py
# @@ -1,2 +1,4 @@
# -def add(a,b):
# -    return a+b
# +def mul(a,b):
# +    return a*b
# +def mul_by_2(a):
# +    print(mul(a,2))
# """
repo = git.Repo("../.")
hcommit = repo.head.commit
diff = hcommit.diff("HEAD~1")
differ = Differ()
for d in diff.iter_change_type('M'):
    print(d.a_path)
    a_text = d.a_blob.data_stream.read().decode('utf-8').splitlines(keepends=True)
    b_text = d.b_blob.data_stream.read().decode('utf-8').splitlines(keepends=True)
    result = list(differ.compare(b_text, a_text))
    pprint(result)

# prompt = ChatPromptTemplate.from_template(
#     """
#     You are a documentation assistant. A code change was just committed.

#     ## Code Change:
#     {code_diff}

#     ## Current Documentation:
#     {prev_docs}

#     Update the documentation to reflect the code change.
#     """
# )

# prompt_input = prompt.format(
#     code_diff = diff,
#     prev_docs = current_docs
# )

# llm = ChatOllama(model="llama3.2", temperature=0.1)
# llm_response = llm.invoke(prompt_input)

# with open(docs_path, "w") as f:
#     f.write(llm_response.content)

repo.__del__()
exit(0)