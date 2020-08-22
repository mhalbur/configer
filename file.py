import os

def check_for_file(file_path='/mnt/data/configuration/configer.yaml'):
    try:
        print(f"Looking for {file_path}")
        os.path.exists(file_path)
        # check_permissions(file_path)
    except:
        print(f"{file_path} does not exist... creating file")
        create_file(file_path)
        

def create_file(file_path):
    os.mknod(file_path)
    # change_permissions(file_path)


def check_permissions(file_path):
    permissions = os.stat(file_path)
    print(permissions)


def change_permissions(file_path):
    os.chmod(file_path, 744)


check_for_file()