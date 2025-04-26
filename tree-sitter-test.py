from dt_diff_lib import tree_sitter_parser_init



comment_py_inline = b"# Hello world"

comment_py_string_literal = b"""'''
This is some random commmentt og :attr bla bla
Este application de computadora 
Es un commento muy facil!
'''"""

comment_js_multiline = b"/* Hello\n* world\n* ! */" 

comment_js_inline = b"// Hello world!"

comment_java_multiline = b"/* Hello \n World\n !*/"

wrong_comment_py_expression= b'a = mul("hello")'

other_wrong = b'''def mul(a, b):
"""this is a comment very nice wrong
"""
'''

comments = []
comments.append((comment_java_multiline,"java"))
comments.append((comment_js_inline, "javascript"))
comments.append((comment_js_multiline, "javascript"))
comments.append((comment_py_inline,"python"))
comments.append((comment_py_string_literal,"python"))
comments.append((wrong_comment_py_expression, "python"))
comments.append((other_wrong,"python"))


for comment, language in comments:
    root = tree_sitter_parser_init(language, comment)
    print(root.type)
    print(root.children)
    child = root.children[0]
    if child.type in ["comment", "block_comment"] or (child.type == "expression_statement" and child.children[0].type == "string" and ((child.children[0].text.startswith(b'"""') and child.children[0].text.endswith(b'"""')) or (child.children[0].text.startswith(b"'''") and child.children[0].text.endswith(b"'''")))):
        print("Inside if")
        

#(child.children[0].text.startswith('"""') and child.children[0].text.endswith('"""')