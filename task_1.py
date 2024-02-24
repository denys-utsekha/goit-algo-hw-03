import sys
import os
from pathlib import Path
import shutil

args = sys.argv

if len(args) < 2:
    print("Введіть назву папки з якої має відбутись копіювання.")
    sys.exit(1)

old_folder = args[1]
new_folder = "dist"
if len(args) > 2:
    new_folder = args[2]


def read_dir(path: Path):
    try:
        if path.is_dir():
            for child in path.iterdir():
                read_dir(child)
        else:
            file_extension = os.path.splitext(path)[1]
            if file_extension:
                file_path = f"{new_folder}/{file_extension.split(".")[1]}"
                if not os.path.exists(file_path):
                    os.makedirs(file_path)
                try:
                    shutil.copy2(path, file_path)
                except Exception as error:
                    print(error)
    except Exception as error:
        print(error)


if os.path.exists(old_folder):
    read_dir(Path(old_folder))
else:
    print(f"За цим шляхом '{old_folder}' нічого не знайдено.")
