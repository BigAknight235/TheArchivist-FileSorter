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
    # TODO: implement input prompt + validation
    raise NotImplementedError


def ensure_category_folders(source_dir: str, categories: Dict[str, List[str]]) -> None:
    """
    Ensure every standardized category folder (keys of CENTRAL_CATEGORIES)
    exists at the top level inside source_dir. Create if missing.
    """
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
    # 1) Get and validate source directory
    # source_dir = get_source_directory()
    # 2) Ensure standardized category folders exist
    # ensure_category_folders(source_dir, CENTRAL_CATEGORIES)
    # 3) Phase 1
    # standardize_folders(source_dir, CENTRAL_CATEGORIES)
    # 4) Phase 2
    # sort_items(source_dir, CENTRAL_CATEGORIES)
    # 5) Catch-All
    # move_to_unsorted(source_dir, unsorted_key="10_Unsorted")
    # 6) Summary / optional dry-run support
    raise NotImplementedError


if __name__ == "__main__":
    main()