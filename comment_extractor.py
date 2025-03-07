from tree_sitter import Parser
from tree_sitter_languages import get_language
from remove_comments import remove_comments

parser = Parser()
def init_parser(code_language):
    language = get_language(code_language)
    parser.set_language(language)

def parse_code(code):
    return parser.parse(bytes(code, "utf8"))

def extract_comments_and_code_pairs(code, code_language):
    tree = parse_code(code)
    root_node = tree.root_node
    
    comments = []
    comment_code_pairs = []
    
    # First, clean the entire source code
    # cleaned_full_code = remove_comments(code_language, code.encode("utf-8")).decode("utf-8")
    
    # Traverse AST to find comments and associate them with nearest code blocks
    def traverse(node):
        nonlocal comments, comment_code_pairs
        
        if node.type in ["comment", "block_comment"]:
            comment_text = code[node.start_byte:node.end_byte].strip()
            
            # If the last comment is right above the current one, merge them
            if comments and comments[-1][1] == node.start_byte - 1:
                comments[-1] = (comments[-1][0] + "\n" + comment_text, comments[-1][1])
            else:
                comments.append((comment_text, node.start_byte))
        
        elif node.type in ["function_definition", "class_definition", "expression_statement", "assignment"]:
            code_text = code[node.start_byte:node.end_byte].strip()
            
            if comments:
                combined_comment = "\n".join(c[0] for c in comments)
                clean_code_text = remove_comments(code_language, code_text.encode("utf-8")).decode("utf-8")
                comment_code_pairs.append((combined_comment, clean_code_text))
                comments = []  # Reset comments after assignment
        
        for child in node.children:
            traverse(child)
    
    traverse(root_node)
    
    return comment_code_pairs

def extract_from_content(github_content, code_language):
    init_parser(code_language)
    code = github_content.decoded_content.decode("utf-8")
    return extract_comments_and_code_pairs(code, code_language)

if __name__ == "__main__":
    print("This module is meant to be imported and used with GitHub content.")
