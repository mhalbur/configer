import os
import yaml

class File():
    def __init__(self, project_config=None):
        self.project_config = project_config


    def create_file(self, filepath):
        basedir = os.path.dirname(filepath)
        if not os.path.exists(basedir):
            os.makedirs(basedir)
        with open(filepath, 'w') as f:
            pass
        
            
    def file_to_dict(self, filepath=None):
        if filepath is None:
            filepath = self.project_config
    
        with open(filepath, 'r+') as c_file:
            yaml_dict=yaml.safe_load(c_file)
            
        return yaml_dict

