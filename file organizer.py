import os
import shutil

folder = "/Users/name/Downloads"

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".tar"]
}

for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)

    if os.path.isdir(file_path):
        continue

    name, extension = os.path.splitext(filename)
    moved = False

    for category, extensions in file_types.items():
        if extension.lower() in extensions:
            target_folder = os.path.join(folder, category)
            os.makedirs(target_folder, exist_ok=True)
            target_path = os.path.join(target_folder, filename)
            shutil.move(file_path, target_path)
            moved = True
            break

    if not moved:
        other_folder = os.path.join(folder, "Others")
        os.makedirs(other_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(other_folder, filename))
