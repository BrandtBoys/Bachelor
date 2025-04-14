import sys
from uuid import uuid4
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import git #gitPython
import os
import time
from tree_sitter import Parser, Node
from tree_sitter_languages import get_language
import detect_language
from dt_diff_lib import extract_data, collect_code_comment_range, tree_sitter_parser_init


repo = git.Repo(".")

#to accommodate test-environment: the test script manages branch name and creation
branch_id = uuid4()
branch_name = "Update-docs-" + str(branch_id)
repo.git.branch(branch_name)
repo.git.checkout(branch_name)


# Set the branch name in the GitHub Actions environment
with open(os.getenv('GITHUB_ENV'), "a") as env_file:
    env_file.write(f"BRANCH_NAME={branch_name}\n")

# Compare changes and find changed files
hcommit = repo.head.commit

diff_files = list(hcommit.diff("HEAD~1"))

for file in diff_files:
    source_path = str(file.a_path)
    print("Generating comments for diffs in" + source_path)
    file_language = detect_language.detect_language(source_path)
    if not file_language:
            continue
    h1_content = ""
    try:
        h1_commit = repo.commit("HEAD~1")
        h1_blob = h1_commit.tree / source_path
        h1_content = h1_blob.data_stream.read().decode("utf-8")
    except Exception as e:
        print(e)
        print("new file incoming!!")


    with open(source_path, "r") as f:
        source_code = f.read()

    # Extract all function which is in the diff
    code_location = extract_data(True, file_language, h1_content, source_code, collect_code_comment_range)

    comment_location =[]
    for code, old_comment, start_byte, end_byte in code_location:

        print(old_comment)

        # Create prompt for LLM
        prompt = ChatPromptTemplate.from_template(
            """
            You are a documentation assistant.

            ## Instructions:
            - Given the code, make an **only** descriptive comment of the function
            - follow best comment practice regrading to the file language
            - if there is a old comment, update that to reflect the changes to the function
            - your answer will be directly inserted into code of type file language, so you answer has to be able to compile in the give file language
            - do **not** include the function definition in your answer

            ##file language:
            {file_language}

            ## Code:
            {code}

            ## Old comment:
            {old_comment}

            Return **only** the comment:
            """
        )

        prompt_input = prompt.format(
            code = code,
            file_language = file_language,
            old_comment = old_comment
        )

        start = time.time()
        # the LLM does it work
        llm = ChatOllama(model="llama3.2", temperature=0.1)
        llm_response = llm.invoke(prompt_input)
        end = time.time()
        # print(f"LLM took {end - start:.4f} seconds")
        # print(llm_response.content)
        comment_location.append(((llm_response.content), start_byte, end_byte))

    commented_code = bytearray(source_code.encode("utf-8"))
    for comment, start_byte, end_byte in reversed(comment_location):
        commented_code[start_byte:end_byte] = (comment+"\n").encode()

    # Write changes to docs
    with open(source_path, "w") as f:
        f.write(commented_code.decode("utf-8"))

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