from agent import run_llm, generate_llm_response, validate_response_as_comment
from dt_diff_lib import extract_data, collect_code_comment_range


def test_llm():

    #Arrange
    with open("./test_files_from_flask/cli_6c44dd4.py","r") as f:
        h1 = f.read()
    
    with open("./test_files_from_flask/cli_2c31603.py","r") as f:
        source = f.read()

    #Act
    result = run_llm("python" ,h1, source)

    #Assert
    assert result

def test_each_llm_call():
    # Arrange
    with open("./test_files_from_flask/cli_6c44dd4.py", "r") as f:
        h1_content = f.read()
    
    with open("./test_files_from_flask/cli_2c31603.py", "r") as f:
        source_code = f.read()
    
    code_location = extract_data(True, "python", h1_content, source_code, collect_code_comment_range)

    failures = []
    results = []  # Keep all results to print later
    code_location_len = len(code_location)

    # Act & track
    for i, (code, old_comment, start_byte, end_byte) in enumerate(code_location, start=1):
        print(f"Function {i} out of {code_location_len}")
        llm_response = generate_llm_response("python", code, old_comment)

        is_valid = validate_response_as_comment("python", llm_response.content)
        
        results.append({
            "index": i,
            "code": code.splitlines()[0],
            "comment": llm_response.content,
            "valid": is_valid
        })

        if not is_valid:
            failures.append(i)

    # ✅ Final summary printout
    for r in results:
        status = "SUCCESS" if r["valid"] else "FAILURE"
        print(f"\n--- {status} #{r['index']} ---")
        print("For func def:")
        print(r["code"])
        print("\n Generated Comment:")
        print(r["comment"])

    # Final assertion
    if failures:
        assert False, f"{len(failures)} comment(s) failed validation"



# def test_each_llm_call():
    
#     #Arrange
#     with open("./test_files_from_flask/cli_6c44dd4.py","r") as f:
#         h1_content = f.read()
    
#     with open("./test_files_from_flask/cli_2c31603.py","r") as f:
#         source_code = f.read()
    
#     code_location = extract_data(True, "python", h1_content, source_code, collect_code_comment_range)
#     code_location = []

#     counter = 1
#     code_location_len = len(code_location)
#     #Act

#     for code, old_comment, start_byte, end_byte in code_location:
#         print(f"function {counter} out of {code_location_len}")
#         llm_response = generate_llm_response("python",code,old_comment)

#         #Assert
#         test_comment_validity("python", llm_response)

# def test_comment_validity(file_language, comment):

#     #Assert
#     validate_response_as_comment(file_language, comment)

