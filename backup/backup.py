import os
import shutil
from datetime import datetime

source_dir = input("Please Enter path of a Source Directory\n")
dest_dir = input("Please Enter path of a Destination Directory\n")

def backup(source_dir,dest_dir):
    if not os.path.isdir(source_dir):
        print(f"Error:Invalid Source directory ")
        return

    if not os.path.isdir(dest_dir):
        print(f"Error: Invalide Destination Directory")
        return

    for filename in os.listdir(source_dir):
        src_file = os.path.join(source_dir, filename)

        if os.path.isfile(src_file):
            dest_file = os.path.join(dest_dir, filename)

            # Rename if file already exists in destination
            if os.path.exists(dest_file):
                base, ext = os.path.splitext(filename)
                print(base,ext)
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                filename = f'{base}_{timestamp}{ext}'
                dest_file = os.path.join(dest_dir, filename)

            try:
                shutil.copy2(src_file, dest_file)
                print(f"Copied: {src_file} -> {dest_file}")
            except Exception as e:
                print(f"Failed to copy '{src_file}': {e}")


backup(source_dir,dest_dir)