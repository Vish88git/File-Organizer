import shutil
from pathlib import Path  # Helps us work with folders and files

CATEGORY_MAP = {
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".doc"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
}


def get_category(ext: str) -> str:
    """Return the category name for a given file extension."""
    ext = ext.lower()
    for category, extensions in CATEGORY_MAP.items():
        if ext in extensions:
            return category
    return "Others"   # default if no match


def organize_folder(folder_path: Path) -> None:
    """Organize files in the given folder into category subfolders."""
    print("Looking Inside:", folder_path)

    if not folder_path.exists() or not folder_path.is_dir():
        print("[ERROR] Folder does not exist or is not a directory.")
        return

    for item in folder_path.iterdir():
        if item.is_file():
            ext = item.suffix.lower()
            category = get_category(ext)

            # Build the folder for this category
            target_dir = folder_path / category

            # Create the folder if it does not exist
            if not target_dir.exists():
                print("Creating Folder:", target_dir)
                target_dir.mkdir(parents=True, exist_ok=True)

            # Build the full target path (folder + file name)
            target_path = target_dir / item.name

            print(f"Moving: {item.name} → {category}/")
            shutil.move(str(item), str(target_path))

    print("\nDone organizing! ✅")


def main():
    # Ask user for a folder path
    user_input = input("Enter the path of the folder to organize: ").strip()

    # Convert string to Path
    folder_path = Path(user_input)

    organize_folder(folder_path)


if __name__ == "__main__":
    main()

