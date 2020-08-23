import os

"""
ToDo List
- Determine permissions on the file? If in repo - do we want more limited permissions? 400?
"""

def check_for_file(file_path='configuration/configer.yaml'):
    try:
        print(f"Looking for {file_path}")
        os.path.exists(file_path)
        check_permissions(file_path)
        print(f"{file_path} exists!")
    except:
        create_file(file_path)
        

def create_file(file_path):
    print(f"{file_path} does not exist... creating file.")
    os.mknod(file_path)
