import os

# Mapping of file extensions to programming languages
EXTENSION_TO_LANGUAGE = {
    ".py": "python",
    ".java": "java",
    # Added ".js" extension for JavaScript
    ".js": "javascript",
    # Added ".ts" extension for TypeScript
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
    # Added ".yml" extension for YAML
    ".yml": "yaml",
    ".r": "r",
    ".pl": "perl",
    ".lua": "lua",
    ".dart": "dart",
    ".scala": "scala"
}

def detect_language(filename):
    """
    Detects programming language based on file extension.
    
    The function works by splitting the filename into a base and an extension, 
    then looking up the extension in the EXTENSION_TO_LANGUAGE dictionary. 
    If the extension is found, its corresponding language is returned; otherwise, "unknown" is returned.
    """
    _, ext = os.path.splitext(filename)  # Extract file extension
    return EXTENSION_TO_LANGUAGE.get(ext, None)  # Return language or "unknown"