# TheArchivist-FileSorter
The Archivist is a smart Python file organizer designed to bring semantic order to chaotic directories. It sorts files and standardizes existing folders based on predefined categories and keywords, not just file extensions.
## 💡 The Problem & The Innovation

Traditional file sorters rely solely on file extensions (e.g., separating all `.pdf`s). This approach fails when directories contain poorly-named folders (like "old games folder") or when items need to be grouped by purpose (e.g., all Steam and Epic Games files into a single "Games" category).

**The Archivist** solves this by implementing a two-phase, keyword-driven sorting system:

1.  **Phase 1: Folder Standardization:** It iterates through existing folders and relabels them based on keywords found in their names (e.g., renaming "My Budget Reports" to `02_Documents`).
2.  **Phase 2: Semantic Sorting:** It matches files and unclassified folders against a central keyword configuration (e.g., matching the filename "Cyberpunk 2077 Shortcut.lnk" to the `01_Games` category).

All items are sorted into a standardized, numbered directory structure.
## 🚀 Quick Start

### Prerequisites
*  **Python 3.x**

### Installation and Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/TheArchivist-FileSorter.git](https://github.com/YOUR_USERNAME/TheArchivist-FileSorter.git)
    cd TheArchivist-FileSorter
    ```
2.  Run the script:
    ```bash
    python the_archivist.py
    ```
3.  The script will prompt you to enter the full path of the directory you wish to organize.

**Note:** Always run The Archivist on a copy of a directory first, or review the source code to understand its file moving logic before applying it to critical system folders.
## ⚙️ Configuration

The core logic is driven by the `CENTRAL_CATEGORIES` dictionary within `the_archivist.py`. This structure allows for easy customization and demonstrates clean separation of concerns.

The standardized folder names use **numerical prefixes** (e.g., `01_Games`) to ensure logical sorting in every file explorer.

**Example Snippet:**

| Standardized Folder | Keywords/Extensions that trigger a match |
| :--- | :--- |
| `01_Games` | `steam`, `epic`, `.lnk`, `game` |
| `02_Documents` | `.pdf`, `report`, `resume`, `.docx` |
| `10_Unsorted` | (The final fallback for any unclassified item) |
## 🎯 Future Development

Planned enhancements include:
* Adding support for external/network drive paths.
* Implementing a `--dry-run` flag to preview changes before execution.
* Creating a simple graphical user interface (GUI).

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.