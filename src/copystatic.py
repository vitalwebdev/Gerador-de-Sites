import os
import shutil

def recursive_copy_files(source_path, final_path):
    if not os.path.exists(final_path):
        os.mkdir(final_path)
        
    for filename in os.listdir(source_path):
        from_path = os.path.join(source_path, filename)
        dest_path = os.path.join(final_path, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            recursive_copy_files(from_path, dest_path)