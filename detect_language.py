import os

# Mapping of file extensions to programming languages
EXTENSION_TO_LANGUAGE = {
    ".py": "python",
    ".java": "java",
    # Added '.js' extension for JavaScript
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
    ".yml": "yaml",  # Added '.yml' extension for YAML
    ".r": "r",
    ".pl": "perl",
    ".lua": "lua",
    ".dart": "dart",
    ".scala": "scala"
}

# Function to detect programming language based on file extension
def detect_language(filename):
    """
    Detects programming language based on file extension.
    
    The function uses the os.path.splitext() method to extract the file extension from the filename.
    It then looks up the corresponding language in the EXTENSION_TO_LANGUAGE dictionary and returns it.
    If the file extension is not found, it returns 'unknown'.
    """
    _, ext = os.path.splitext(filename)  # Extract file extension
    return EXTENSION_TO_LANGUAGE.get(ext, None)  # Return language or 'unknown'