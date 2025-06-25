import os
import shutil

def static_to_public(src_path, dest_path):
    if os.path.exists(dest_path):
        shutil.rmtree(dest_path)
        os.makedirs(dest_path)
        print(f"Path exists, deleting and creating new path: {dest_path}...")
    else:
        os.mkdir(dest_path)
        print(f"Path doesn't exist, creating new path: {dest_path}...")

    for item in os.listdir(src_path):
        src_item = os.path.join(src_path, item)
        dest_item = os.path.join(dest_path, item)

        if os.path.isfile(src_item):
            shutil.copy(src_item, dest_item)
            print(f"Path {src_item} is a file, copying {src_item} to {dest_item}...")
        elif os.path.isdir(src_item):
            static_to_public(src_item, dest_item)
            print(f"Path {src_item} is a directory, recursing...")
        else:
            print("Non-item / non-directory found, skipping...")
            continue
