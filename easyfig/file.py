import os
import yaml

class File():
    def __init__(self, config_file=None):
        self.project = f"{os.getcwd().split('\\')[-1]}"
        self.config_file=f'{self.project}_Config.yaml' if config_file is None else config_file 
        self.config_filepath=f'configuration\\{self.config_file}'
        print("4: ", self.config_file)

    def create_file(self):
        basedir = os.path.dirname(self.config_filepath)
        if not os.path.exists(basedir):
            os.makedirs(basedir)
        with open(self.config_filepath, 'w') as f:
            pass

    def file_to_dict(self):
        with open(self.config_filepath, 'r') as c_file:
            yaml_dict=yaml.safe_load(c_file)
            
        return yaml_dict

