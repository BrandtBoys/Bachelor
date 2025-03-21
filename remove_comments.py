from tree_sitter import Parser
from tree_sitter_languages import get_language

def remove_comments(code_language, source_code):
    parser = Parser()
    language = get_language(code_language)
    parser.set_language(language)
    tree = parser.parse(source_code)
    root_node = tree.root_node

    comment_placement = []

    def find_comment_placement(node, code):
        """Recursively collects the byte placement of any comments in a given source code"""
        
        
        if node.type == "comment":  # finds node types of comment and append there byte start and end to the list
            comment_placement.append((node.start_byte,node.end_byte))
        
        # Recursively process children
        for child in node.children:
            find_comment_placement(child, code)
        
    find_comment_placement(root_node, source_code)

    cleaned_source = bytearray(source_code)
    for start, end in reversed(comment_placement): 
        cleaned_source[start:end] = b""
    return cleaned_source

    