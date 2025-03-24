import os

# Mapping of file extensions to programming languages
EXTENSION_TO_LANGUAGE = {
    ".py": "python",  # Python files have this extension
    ".java": "java",  # Java files have this extension
    ".js": "javascript",  # JavaScript files have this extension
    ".ts": "typescript",  # TypeScript files have this extension
    ".c": "c",  # C files have this extension
    ".cpp": "cpp",  # C++ files have this extension
    ".cs": "csharp",  # C# files have this extension
    ".rb": "ruby",  # Ruby files have this extension
    ".php": "php",  # PHP files have this extension
    ".go": "go",  # Go files have this extension
    ".rs": "rust",  # Rust files have this extension
    ".swift": "swift",  # Swift files have this extension
    ".kt": "kotlin",  # Kotlin files have this extension
    ".sh": "shell",  # Shell scripts have this extension
    ".html": "html",  # HTML files have this extension
    ".css": "css",  # CSS files have this extension
    ".json": "json",  # JSON files have this extension
    ".xml": "xml",  # XML files have this extension
    ".yaml": "yaml",  # YAML files have this extension
    ".yml": "yaml",  # YAML files also have this extension
    ".r": "r",  # R files have this extension
    ".pl": "perl",  # Perl files have this extension
    ".lua": "lua",  # Lua files have this extension
    ".dart": "dart",  # Dart files have this extension
    ".scala": "scala"  # Scala files have this extension
}

# Detects programming language based on file extension.
def detect_language(filename):
    """Detects programming language based on file extension."""
    _, ext = os.path.splitext(filename)  
    return EXTENSION_TO_LANGUAGE.get(ext, None)