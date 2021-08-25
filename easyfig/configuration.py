import os
import yaml
from cryptography.fernet import Fernet
from pathlib import Path
from .file import File


class EasyConfig_Config():
    def __init__(self):
        self.user_home_directory=str(Path.home())
        self.easyfig_config=f'{self.user_home_directory}/.easyfig_config'  


    def create_easyfig_config(self):
        os.mknod(self.easyfig_config)


    def create_key(self, keypath):
        if os.path.exists(keypath) is False:
            self.generate_key(keypath=keypath)


    def generate_key(self, keypath):
        configer_key=Fernet.generate_key()
        with open(keypath, "wb") as key_f:
            key_f.write(configer_key)

    
    def setup(self, keypath=None):
        if keypath is None:
            keypath=f"{self.user_home_directory}/.easyfig_secret"

        self.create_key(keypath=keypath)
        self.create_easyfig_config()
        self.easyfig_config_write(key='easyfig_key', filepath=keypath)


    def name_repo_config(self):
        current_directory=os.getcwd().split('/')[-1]
        return f'{self.user_home_directory}/configuration/{current_directory}_config.yaml'


    def create_repo_config(self, filepath=None):
        if filepath is None:
            filepath=self.name_repo_config()
        File().create_file(filepath=filepath)
        self.easyfig_config_write(key=os.getcwd().split('/')[-1], filepath=filepath)
        return filepath


    def easyfig_config_write(self, key, filepath):
        yaml_dict=File().file_to_dict(filepath=self.easyfig_config) or {}
        yaml_dict[key]=filepath

        with open(self.easyfig_config, 'w') as c_file:
            yaml.dump(yaml_dict, c_file)
