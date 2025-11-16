from pathlib import Path

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Code": [".py", ".html", ".js", ".css"],
    "Archives": [".zip", ".rar", ".7z"]
}




DOWNLOAD_PATH = Path.home() / "Downloads"
LOG_FILE = DOWNLOAD_PATH / "organizer_log.txt"

#decide category from extension 
def get_category(ext):
    for name, extensions in FILE_TYPES.items():
        if ext in extensions:
            return name
    
    return"Other"

def organize_files(dry_run = True):
    # 1. get the downloads folder path
    DOWNLOAD_PATH = Path.home() / "Downloads"    
    # 2. loop through each item
    for item in DOWNLOAD_PATH.iterdir():
    # 3. skip folders
        if item.is_file():
    # 4. extract extension
            ext = item.suffix.lower()
    # 5. call get_category(ext)
            category = get_category(ext)

            target_folder = DOWNLOAD_PATH / category
            target_folder.mkdir(exist_ok=True)
            targe_path = target_folder / item.name

            if dry_run:
                print(f"[DRY-RUN] {item.name} → {category} (would move)")

            else:
                item.rename(target_path)
                print(f"[MOVED] ")




if __name__ == "__main__":
    organize_files()