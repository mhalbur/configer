import os
import yaml

class File():
    def __init__(self, configer_directory=None, configer_file=None):
        self.configer_directory=configer_directory
        self.configer_file_path=f"{configer_directory}/{configer_file}"


    def create_file(self, filepath):
        basedir = os.path.dirname(filepath)
        if not os.path.exists(basedir):
            os.makedirs(basedir)
        with open(filepath, 'w') as f:
            pass
        
            
    def file_to_dict(self, filepath=None):
        if filepath is None:
            filepath = self.configer_file_path 
    
        with open(filepath, 'r+') as c_file:
            yaml_dict=yaml.safe_load(c_file)
            
        return yaml_dict


    def check_for_key(self, obj, key):
        yaml_dict=self.file_to_dict()
        key_in_file=False
        if obj in yaml_dict:
            if key in yaml_dict[obj]:
                key_in_file=True
        return key_in_file


