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

def organize_files():
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
    # 6. print file + category
            print(f"file: {item.name} → {category}")



if __name__ == "__main__":
    organize_files()