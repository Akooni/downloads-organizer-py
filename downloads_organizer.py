from pathlib import Path
import mimetypes

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Code": [".py", ".html", ".js", ".css"],
    "Archives": [".zip", ".rar", ".7z"]
}




download_path = Path.home() / "Downloads"


for item in download_path.iterdir():
    if item.is_file():
        ext = item.suffix.lower()
        category = "Other"


        for cat_name,extensions in file_types.items():
            if ext in extensions:
                category = cat_name
                break

        print(f"file: {item.name} | ext: {ext} | category: {category}")