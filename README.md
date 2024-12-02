# Line Counter Script

A simple Python script to count the total number of lines of code in a project. This script displays file-wise progress, calculates language-specific line counts, and excludes specified directories from the count.

## Features

- Counts lines of code for files with specific extensions.
- Excludes certain directories (e.g., `node_modules`, `dist`) by default.
- Displays the processing progress and a summary of the results.
- Supports custom file extensions and directory exclusions.

## How to Use

### Prerequisites

- Python 3.6 or higher installed on your system.

### Running the Script

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/line-counter-script.git
   cd line-counter-script
   ```

2. Run the script:
   ```bash
   python count_lines.py
   ```

### Customization

You can customize the script by modifying the following parameters in the `count_lines_of_code` function:

- **`root_dir`**: The root directory to scan (default is `.`).
- **`include_extensions`**: A list of file extensions to include in the count (e.g., `.ts`, `.tsx`, `.js`).
- **`exclude_dirs`**: A list of directories to exclude from the scan (e.g., `node_modules`, `.git`).

#### Example Usage

```python
count_lines_of_code(
    root_dir="path/to/your/project",
    include_extensions=[".py", ".html", ".css"],
    exclude_dirs=["node_modules", "build", ".git"]
)
```

### Output Example

```
Processing (1 of 15): ./src/main.ts
Processing (2 of 15): ./src/helpers/util.ts
Processing (3 of 15): ./src/components/Button.tsx
...
Processing (15 of 15): ./src/styles/global.css

Summary:
Total files processed: 15
Total lines of code: 2,143

Lines of code by file type:
  .ts: 1,200 (5 files)
  .tsx: 650 (7 files)
  .css: 200 (2 files)
  .json: 93 (1 file)

Excluded directories:
  - node_modules
  - .git
  - dist

Files processed:
  1. ./src/main.ts: 500 lines
  2. ./src/helpers/util.ts: 200 lines
  3. ./src/components/Button.tsx: 150 lines
  ...
  15. ./src/styles/global.css: 50 lines
```

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you'd like to improve this script.

## License

This project is licensed under the [MIT License](LICENSE).
