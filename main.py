import os

def count_lines_of_code(root_dir=".", include_extensions=None, exclude_dirs=None):
    """
    Count the total number of lines of code in a project, showing file-wise progress and language-specific line counts.

    Parameters:
    - root_dir (str): The root directory to scan (default is the current directory).
    - include_extensions (list): List of file extensions to include (e.g., ['.js', '.ts', '.tsx']).
    - exclude_dirs (list): List of directories to exclude from counting (e.g., ['node_modules', 'dist']).

    Returns:
    - line_counts (dict): A dictionary of line counts by file extension.
    """
    if include_extensions is None:
        # Default to common code file extensions
        include_extensions = [".js", ".ts", ".tsx", ".mjs", ".json", ".css", ".html"]

    if exclude_dirs is None:
        # Default directories to exclude
        exclude_dirs = ["node_modules", "dist", "build", ".git", "public"]

    # Dictionary to store line counts per file extension
    line_counts = {ext: 0 for ext in include_extensions}
    total_lines = 0
    visited_files = []

    # Collect all relevant files
    files_to_process = []
    for root, dirs, files in os.walk(root_dir):
        # Skip excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]

        for file in files:
            if any(file.endswith(ext) for ext in include_extensions):
                files_to_process.append(os.path.join(root, file))

    # Process each file and count lines
    total_files = len(files_to_process)
    for idx, file_path in enumerate(files_to_process, start=1):
        visited_files.append(file_path)
        try:
            # Count lines in the file
            with open(file_path, "r", errors="ignore") as f:
                line_count = sum(1 for _ in f)
                total_lines += line_count

                # Update count for the file's extension
                for ext in include_extensions:
                    if file_path.endswith(ext):
                        line_counts[ext] += line_count

        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            continue

        # Show progress
        print(f"Processing ({idx} of {total_files}): {file_path}")

    # Print detailed results
    print("\nSummary:")
    print(f"Total files processed: {total_files}")
    print(f"Total lines of code: {total_lines}")
    print("\nLines of code by file type:")
    for ext, count in line_counts.items():
        print(f"  {ext}: {count}")

    return line_counts

if __name__ == "__main__":
    count_lines_of_code(
        root_dir=".",
        include_extensions=[".ts", ".tsx", ".js", ".mjs", ".json", ".css", ".html"],
        exclude_dirs=["node_modules", "dist", ".git", "public"]
    )
