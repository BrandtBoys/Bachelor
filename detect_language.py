import os

# Mapping of file extensions to programming languages
EXTENSION_TO_LANGUAGE = {
    ".py": "python",
    ".java": "java",
    # Added ".js" extension for JavaScript
    ".js": "javascript",  # Maps JavaScript files to the 'javascript' language
    # Added ".ts" extension for TypeScript
    ".ts": "typescript",  # Maps TypeScript files to the 'typescript' language
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
    # Added ".yml" extension for YAML
    ".yml": "yaml",  # Maps YAML files to the 'yaml' language
    ".r": "r",
    ".pl": "perl",
    ".lua": "lua",
    ".dart": "dart",
    ".scala": "scala"
}

# Detects programming language based on file extension
def detect_language(filename):
    """Detects programming language based on file extension."""
    # Extract file extension from the filename
    _, ext = os.path.splitext(filename)  
    # Return language or None if unknown
    return EXTENSION_TO_LANGUAGE.get(ext, None)