"""
Task 1a — Move all .jpg files from source folder to a destination folder.
Uses: os, shutil
"""

import os
import shutil


def move_jpg_files(source_dir: str, dest_dir: str) -> int:
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source folder not found: {source_dir}")

    os.makedirs(dest_dir, exist_ok=True)

    moved = 0
    for filename in os.listdir(source_dir):
        if filename.lower().endswith(".jpg"):
            src = os.path.join(source_dir, filename)
            dst = os.path.join(dest_dir, filename)
            shutil.move(src, dst)
            print(f"  Moved: {filename}")
            moved += 1

    return moved


if __name__ == "__main__":
    source = os.path.join(os.path.dirname(__file__), "sample_folder")
    destination = os.path.join(os.path.dirname(__file__), "images_output")

    print(f"Source     : {source}")
    print(f"Destination: {destination}")
    print("-" * 40)

    count = move_jpg_files(source, destination)
    print("-" * 40)
    print(f"Done. {count} .jpg file(s) moved to '{destination}'.")
