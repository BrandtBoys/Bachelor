from tree_sitter import Parser
from tree_sitter_languages import get_language

def remove_comments(code_language, source_code):
  # Initialize a parser object to parse the source code.
    parser = Parser()
  # Get the language of the source code based on the provided code language.
    language = get_language(code_language)
  # Set the language for the parser.
    parser.set_language(language)
  # Parse the source code into an abstract syntax tree (AST).
    tree = parser.parse(source_code)
  # Get the root node of the AST, which represents the entire source code.
    root_node = tree.root_node

    comment_placement = []

    def find_comment_placement(node, code):
        """Recursively collects the byte placement of any comments in a given source code"""
        
      # Check if the current node is a comment. If it is, append its start and end bytes to the comment placement list.
        
        if node.type == "comment":  
            comment_placement.append((node.start_byte,node.end_byte))
        
    # Recursively process children of the current node.
        
        for child in node.children:
            find_comment_placement(child, code)
        
  # Start the recursive search from the root node.
    find_comment_placement(root_node, source_code)

  # Create a copy of the original source code as a bytearray.
    cleaned_source = bytearray(source_code)
  # Iterate over the comment placements in reverse order (from end to start).
    for start, end in reversed(comment_placement): 
      # Replace the bytes between the start and end indices with an empty byte array.
        cleaned_source[start:end] = b""
  # Return the cleaned source code as a bytearray.
    return cleaned_source

    