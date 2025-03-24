from tree_sitter import Parser
from tree_sitter_languages import get_language
 
def remove_comments(code_language, source_code):
    # Create a parser instance and set its language based on the provided code language
    parser = Parser()
    language = get_language(code_language)
    parser.set_language(language)
    
    # Parse the source code into an abstract syntax tree (AST) to analyze comments
    tree = parser.parse(source_code)
    root_node = tree.root_node
    
    comment_placement = []
    
    def find_comment_placement(node, code):
        """Recursively collects the byte placement of any comments in a given source code"""
        
        # Check if the current node is a comment and extract its start and end bytes
        if node.type == "comment":  
            comment_placement.append((node.start_byte,node.end_byte))
        
    # Recursively process children to analyze nested comments
    for child in node.children:
        find_comment_placement(child, code)
    
    # Start the recursive analysis from the root node of the AST
    find_comment_placement(root_node, source_code)
    
    # Clean the source code by removing comments and return the cleaned bytes
    cleaned_source = bytearray(source_code)
    for start, end in reversed(comment_placement): 
        cleaned_source[start:end] = b""
    return cleaned_source