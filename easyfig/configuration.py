import os
import sys
import yaml
from os.path import exists
from cryptography.fernet import Fernet
from pathlib import Path
from .file import File


class EasyConfig_Config():
    def __init__(self, config_file=None):
        self.user_home_directory=str(Path.home())
        self.current_directory = os.getcwd()
        self.project = f"{os.getcwd().split('/')[-1]}"
        self.config_file=f'{self.project}_Config.yaml' if config_file is None else config_file  
        self.config_filepath=self.config_filepath=f'configuration/{self.config_file}'
        self.easyfig_keypath=f"{self.user_home_directory}/.easyfig_secret"
        

    def create_easyfig_config(self):
        os.mknod(self.config_filepath)

    def create_key(self, keypath):
        if os.path.exists(keypath) is False:
            self.generate_key(keypath=keypath)

    def generate_key(self, keypath):
        configer_key=Fernet.generate_key()
        with open(keypath, "wb") as key_f:
            key_f.write(configer_key)

    def setup(self):
        self.create_key(keypath=self.easyfig_keypath)
        self.create_easyfig_config()
        self.easyfig_config_write(key='easyfig_key', filepath=self.easyfig_keypath)

    def name_project_config(self):
        return self.easy_config

    def create_project_config(self, filepath=None):
        if filepath is None:
            filepath=self.name_project_config()
        File().create_file(filepath=filepath)
        self.easyfig_config_write(key=self.project, filepath=filepath)
        return filepath

    def easyfig_config_write(self, key, filepath):
        yaml_dict=File().file_to_dict(filepath=self.config_filepath) or {}
        yaml_dict[key]=filepath

        with open(self.config_filepath, 'w') as c_file:
            yaml.dump(yaml_dict, c_file)

    def get_project_path(self):
        file_exists = exists(self.config_filepath)
        if file_exists:
            return self.config_filepath
        else:
            print("Unable to locate project configuration. Please run 'easyfig projectconfiger' to create it.")
            return 'exit'

    def get_key_path(self):
        file_exists = exists(self.easyfig_keypath)
        if file_exists:
            return self.easyfig_keypath
        else:
            print("Unable to locate project configuration. Please run 'easyfig setup' to create it.")
            return 'exit'
