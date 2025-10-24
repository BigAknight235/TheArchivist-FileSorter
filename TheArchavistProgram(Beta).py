import os
import shutil
from typing import Dict, List, Optional

"""
The Archivist - Script Outline
Single central dictionary of standardized category folders -> keywords & extensions.
Uses: os, shutil
This is an outline/skeleton. Fill in implementation details where noted.
"""


# CENTRAL CONFIGURATION: single, central dictionary
CENTRAL_CATEGORIES: Dict[str, List[str]] = {
    "01_Games": ["steam", "epic", ".lnk", ".exe", "game"],
    "02_Documents": [".pdf", ".doc", ".docx", ".txt", "resume", "report"],
    "03_Images": [".png", ".jpg", ".jpeg", ".gif", "screenshot", "photo"],
    "04_Videos": [".mp4", ".mkv", ".mov", "video", "movie"],
    "05_Audio": [".mp3", ".wav", ".flac", "music", "podcast"],
    "06_Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "07_Applications": [".msi", ".exe", ".app", "installer"],
    "08_Projects": ["project", "workspace", ".py", ".js", ".java"],
    "09_Torrents": [".torrent", "torrent"],
    "10_Unsorted": []  # catch-all target
}

# -------------------------
# Configuration / Prep
# -------------------------
def get_source_directory() -> str:
    """
    Prompt user for source directory. Validate path exists and is a directory.
    Return absolute path.
    """
    while True:
        #Prompt user for input
        path = input("Enter the directory path to organize: ").strip()
        
        # Check if path exists
        if not os.path.exists(path):
            print(f"Error: The path '{path}' does not exist. Please try again.")
            continue
          
        # Check if path is a directory
        if not os.path.isdir(path):
            print(f"Error: The path '{path}' is not a directory. Please enter a valid directory path.")
            continue
        
        #Return the absolute path validated
        return os.path.abspath(path)
    # TODO: implement input prompt + validation
    raise NotImplementedError


def ensure_category_folders(source_dir: str, categories: Dict[str, List[str]]) -> None:
    """
    Ensure every standardized category folder (keys of CENTRAL_CATEGORIES)
    exists at the top level inside source_dir. Create if missing.
    """
    for cat in categories:
        #Skip the unsorted folder for now if you want it created later, but including it is safe
        #Create the full path for the category folder
        category_path = os.path.join(source_dir, cat)
        
        #Create the directory. exist_ok=True prevents error if it already exists
        try:
            os.makedirs(category_path, exist_ok=True)
            #You can add a print statement here for logging, e.g.:
            #print(f" [CREATED] import os
import shutil
from typing import Dict, List, Optional

"""
The Archivist - Script Outline
Single central dictionary of standardized category folders -> keywords & extensions.
Uses: os, shutil
This is an outline/skeleton. Fill in implementation details where noted.
"""


# CENTRAL CONFIGURATION: single, central dictionary
CENTRAL_CATEGORIES: Dict[str, List[str]] = {
    "01_Games": ["steam", "epic", ".lnk", ".exe", "game"],
    "02_Documents": [".pdf", ".doc", ".docx", ".txt", "resume", "report"],
    "03_Images": [".png", ".jpg", ".jpeg", ".gif", "screenshot", "photo"],
    "04_Videos": [".mp4", ".mkv", ".mov", "video", "movie"],
    "05_Audio": [".mp3", ".wav", ".flac", "music", "podcast"],
    "06_Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "07_Applications": [".msi", ".exe", ".app", "installer"],
    "08_Projects": ["project", "workspace", ".py", ".js", ".java"],
    "09_Torrents": [".torrent", "torrent"],
    "10_Unsorted": []  # catch-all target
}

# -------------------------
# Configuration / Prep
# -------------------------
def get_source_directory() -> str:
    """
    Prompt user for source directory. Validate path exists and is a directory.
    Return absolute path.
    """
    while True:
        # Prompt user for input
        path = input("Enter the directory path to organize: ").strip()
        
        # Check if path exists
        if not os.path.exists(path):
            print(f"Error: Path '{path}' does not exist. Please try again.")
            continue
            
        # Check if path is a directory
        if not os.path.isdir(path):
            print(f"Error: '{path}' is a file, not a directory. Please provide a folder path.")
            continue
            
        # Return the absolute path once validated
        return os.path.abspath(path)


def ensure_category_folders(source_dir: str, categories: Dict[str, List[str]]) -> None:
    """
    Ensure every standardized category folder (keys of CENTRAL_CATEGORIES)
    exists at the top level inside source_dir. Create if missing.
    """
    for cat in categories:
        # Skip the unsorted folder for now if you want it created later, but including it is safe
        # Create the full path for the category folder
        category_path = os.path.join(source_dir, cat)
        
        # Create the directory. exist_ok=True prevents error if folder already exists.
        try:
            os.makedirs(category_path, exist_ok=True)
            # You can add a print statement here for logging, e.g.:
            print(f"  [CREATED] {cat}/")
        except OSError as e:
            print(f"Warning: Could not create directory {cat} due to error: {e}")


# -------------------------
# Matching Helpers
# -------------------------
def match_category_by_name(name: str, categories: Dict[str, List[str]]) -> Optional[str]:
    """
    Case-insensitive matching of name (folder name or filename without path)
    against keywords in categories.
    Return standardized category key if found, otherwise None.

    Matching strategy (outline):
    - Lowercase the name.
    - For each category, check if any keyword is substring of name.
    - Also check file extension matches (if name contains a dot and extension keywords exist).
    - Return the first matching category (you may prefer deterministic ordering).
    """
    raise NotImplementedError


def is_standard_category_folder(name: str, categories: Dict[str, List[str]]) -> bool:
    """
    Return True if name is one of the standardized category keys.
    """
    # Returns True if the folder name (e.g., '01_Games') is a key in the dictionary
    return name in categories


# -------------------------
# Phase 1: Folder Standardization (Relabel/Move)
# -------------------------
def standardize_folders(source_dir: str, categories: Dict[str, List[str]]) -> None:
    """
    Iterate through all existing subfolders in source_dir (top-level only or recursively as desired).
    For each subfolder:
      - Use case-insensitive matching against CENTRAL_CATEGORIES keywords.
      - If a match is found, rename the subfolder to the standardized category name
        (handle naming collisions carefully).
      - If the folder is already a standardized folder but is not at the top-level
        (i.e., found nested), move it to top-level standardized location.
    Notes / TODOs:
      - Decide whether to operate only on immediate children or recursively.
      - Use os.rename or shutil.move for rename/move operations.
      - Handle conflicts (existing target folder) by merging contents or moving children.
    """
    # Example skeleton:
    # for entry in os.listdir(source_dir):
    #     path = os.path.join(source_dir, entry)
    #     if os.path.isdir(path):
    #         matched = match_category_by_name(entry, categories)
    #         if matched:
    #             target_path = os.path.join(source_dir, matched)
    #             # If entry already matches the standardized name, ensure it's at top
    #             # else rename/move into target_path
    raise NotImplementedError


# -------------------------
# Phase 2: File & New Item Sorting
# -------------------------
def sort_items(source_dir: str, categories: Dict[str, List[str]]) -> None:
    """
    Iterate through remaining items in source_dir (files and any unclassified folders).
    For each item:
      - Determine destination category via match_category_by_name() using filename and extension.
      - If a destination is found, move the item to that standardized folder using shutil.move().
      - If item looks like a folder and no match found, leave for catch-all phase or attempt recursive matching.
    Important considerations:
      - Skip moving the standardized category folders themselves.
      - Be careful to avoid moving a folder into itself.
      - Use atomic moves where possible; handle exceptions.
    """
    raise NotImplementedError


# -------------------------
# Catch-All
# -------------------------
def move_to_unsorted(source_dir: str, unsorted_key: str = "10_Unsorted") -> None:
    """
    Move any remaining items (that are not standardized category folders) into the catch-all folder.
    """
    # Example:
    # for entry in os.listdir(source_dir):
    #     if entry not in categories: shutil.move(os.path.join(source_dir, entry), os.path.join(source_dir, unsorted_key))
    raise NotImplementedError


# -------------------------
# Main Orchestration
# -------------------------
def main():
    """
    Orchestrates:
     1) Preparation: get directory, ensure category folders.
     2) Phase 1: standardize existing folders (rename/move).
     3) Phase 2: sort files and new items.
     4) Catch-all: move leftovers to '10_Unsorted'.
    Provide logs / summary of changes.
    """

    print("--- The Archivist: File Sorting Script ---")
    print("Starting sorting process...")
    # --- 1) Preparation ---
    try:
        source_dir = get_source_directory()
        printf(f"Source directory set to: {source_dir}")
        
        print("1. Ensuring All the Standardized Category Folders Exist...")
        ensure_category_folders(source_dir, CENTRAL_CATEGORIES)
    except NotImplementedError:
      print("SETUP ERROR: Complete the 'get_source_directory' and 'ensure_category_folders' functions first.")
      return
    except Exception as e:
        print(f"an ERROR occurred during setup: {e}")
        return
      
    # --- 2) Phase 1: Standardize Folders (Relabel/Create/Move) ---
    print("2. Phase 1:Standardizing Existing Folders...")
    # standardize_folders(source_dir, CENTRAL_CATEGORIES)
    
    # --- 3) Phase 2: Sort Files & New Items ---
    print("3. Phase 2: Sorting Files and New Items...")
    # sort_items(source_dir, CENTRAL_CATEGORIES)
    
    # --- 4) Catch-All ---
    print("4. Moving Remaining Items to '10_Unsorted'...")
    # move_to_unsorted(source_dir, unsorted_key="10_Unsorted")
    
    # 6) Summary / optional dry-run support
    print("\n--- The Archivist: Operation Complete ---")


if __name__ == "__main__":
    main())
    # Example:
    # for cat in categories:
    #     os.makedirs(os.path.join(source_dir, cat), exist_ok=True)
    raise NotImplementedError


# -------------------------
# Matching Helpers
# -------------------------
def match_category_by_name(name: str, categories: Dict[str, List[str]]) -> Optional[str]:
    """
    Case-insensitive matching of name (folder name or filename without path)
    against keywords in categories.
    Return standardized category key if found, otherwise None.

    Matching strategy (outline):
    - Lowercase the name.
    - For each category, check if any keyword is substring of name.
    - Also check file extension matches (if name contains a dot and extension keywords exist).
    - Return the first matching category (you may prefer deterministic ordering).
    """
    raise NotImplementedError


def is_standard_category_folder(name: str, categories: Dict[str, List[str]]) -> bool:
    """
    Return True if name is one of the standardized category keys.
    """
    return name in categories


# -------------------------
# Phase 1: Folder Standardization (Relabel/Move)
# -------------------------
def standardize_folders(source_dir: str, categories: Dict[str, List[str]]) -> None:
    """
    Iterate through all existing subfolders in source_dir (top-level only or recursively as desired).
    For each subfolder:
      - Use case-insensitive matching against CENTRAL_CATEGORIES keywords.
      - If a match is found, rename the subfolder to the standardized category name
        (handle naming collisions carefully).
      - If the folder is already a standardized folder but is not at the top-level
        (i.e., found nested), move it to top-level standardized location.
    Notes / TODOs:
      - Decide whether to operate only on immediate children or recursively.
      - Use os.rename or shutil.move for rename/move operations.
      - Handle conflicts (existing target folder) by merging contents or moving children.
    """
    # Example skeleton:
    # for entry in os.listdir(source_dir):
    #     path = os.path.join(source_dir, entry)
    #     if os.path.isdir(path):
    #         matched = match_category_by_name(entry, categories)
    #         if matched:
    #             target_path = os.path.join(source_dir, matched)
    #             # If entry already matches the standardized name, ensure it's at top
    #             # else rename/move into target_path
    raise NotImplementedError


# -------------------------
# Phase 2: File & New Item Sorting
# -------------------------
def sort_items(source_dir: str, categories: Dict[str, List[str]]) -> None:
    """
    Iterate through remaining items in source_dir (files and any unclassified folders).
    For each item:
      - Determine destination category via match_category_by_name() using filename and extension.
      - If a destination is found, move the item to that standardized folder using shutil.move().
      - If item looks like a folder and no match found, leave for catch-all phase or attempt recursive matching.
    Important considerations:
      - Skip moving the standardized category folders themselves.
      - Be careful to avoid moving a folder into itself.
      - Use atomic moves where possible; handle exceptions.
    """
    raise NotImplementedError


# -------------------------
# Catch-All
# -------------------------
def move_to_unsorted(source_dir: str, unsorted_key: str = "10_Unsorted") -> None:
    """
    Move any remaining items (that are not standardized category folders) into the catch-all folder.
    """
    # Example:
    # for entry in os.listdir(source_dir):
    #     if entry not in categories: shutil.move(os.path.join(source_dir, entry), os.path.join(source_dir, unsorted_key))
    raise NotImplementedError


# -------------------------
# Main Orchestration
# -------------------------
def main():
    """
    Orchestrates:
     1) Preparation: get directory, ensure category folders.
     2) Phase 1: standardize existing folders (rename/move).
     3) Phase 2: sort files and new items.
     4) Catch-all: move leftovers to '10_Unsorted'.
    Provide logs / summary of changes.
    """

    print("--- The Archivist: File Sorting Script ---")
    print("Starting sorting process...")
    # --- 1) Preparation ---
    try:
        source_dir = get_source_directory()
        printf(f"Source directory set to: {source_dir}")
        
        print("1. Ensuring All the Standardized Category Folders Exist...")
        ensure_category_folders(source_dir, CENTRAL_CATEGORIES)
    except NotImplementedError:
      print("SETUP ERROR: Complete the 'get_source_directory' and 'ensure_category_folders' functions first.")
      return
    except Exception as e:
        print(f"an ERROR occurred during setup: {e}")
        return
      
    # --- 2) Phase 1: Standardize Folders (Relabel/Create/Move) ---
    print("2. Phase 1:Standardizing Existing Folders...")
    # standardize_folders(source_dir, CENTRAL_CATEGORIES)
    
    # --- 3) Phase 2: Sort Files & New Items ---
    print("3. Phase 2: Sorting Files and New Items...")
    # sort_items(source_dir, CENTRAL_CATEGORIES)
    
    # --- 4) Catch-All ---
    print("4. Moving Remaining Items to '10_Unsorted'...")
    # move_to_unsorted(source_dir, unsorted_key="10_Unsorted")
    
    # 6) Summary / optional dry-run support
    print("\n--- The Archivist: Operation Complete ---")


if __name__ == "__main__":
    main()