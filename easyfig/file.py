import os
import yaml

class File():
    def __init__(self, configer_directory, configer_file):
        self.configer_directory=configer_directory
        self.configer_file_path=f"{configer_directory}/{configer_file}"


    def check_for_directory(self):
        if os.path.isdir(self.configer_directory) is False:
            os.makedirs(self.configer_directory)


    def check_for_file(self):
        self.check_for_directory()

        if os.path.exists(self.configer_file_path) is False:
            os.mknod(self.configer_file_path)
            

    def file_to_dict(self):
        with open(self.configer_file_path, 'r+') as c_file:
            yaml_dict=yaml.safe_load(c_file)
        return yaml_dict


    def check_for_key(self, obj, key):
        yaml_dict=self.file_to_dict()
        key_in_file=False
        if obj in yaml_dict:
            if key in yaml_dict[obj]:
                key_in_file=True
        return key_in_file
