import os

# Mapping of file extensions to programming languages
EXTENSION_TO_LANGUAGE = {
    ".py": "python",
    ".java": "java",
    # Added ".js" extension for JavaScript
    ".js": "javascript",
    ".ts": "typescript",
    ".c": "c",
    ".cpp": "cpp",
    ".cs": "csharp",
    ".rb": "ruby",
    ".php": "php",
    ".go": "go",
    ".rs": "rust",
    ".swift": "swift",
    ".kt": "kotlin",
    ".sh": "shell",
    ".html": "html",
    ".css": "css",
    ".json": "json",
    ".xml": "xml",
    ".yaml": "yaml",
    ".yml": "yaml",  # Added .yml extension for YAML
    ".r": "r",
    ".pl": "perl",
    ".lua": "lua",
    ".dart": "dart",
    ".scala": "scala"
}

# Detects programming language based on file extension
def detect_language(filename):
    """
    Detects programming language based on file extension.
    
    Args:
        filename (str): The name of the file to detect the language for.
    
    Returns:
        str: The detected programming language, or 'unknown' if it cannot be determined.
    """
    # Extract the file extension from the filename
    _, ext = os.path.splitext(filename)  
    # Return the language associated with the file extension, or None if not found
    return EXTENSION_TO_LANGUAGE.get(ext, None)