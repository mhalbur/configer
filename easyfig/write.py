import yaml
from .file import File

class Write():
    def __init__(self, encryption, config_file):
        self.encryption_class=encryption
        self.file = File(config_file)
        self.config_file = self.file.config_file
        self.config_filepath = self.file.config_filepath

    def set_value(self, obj, key, value, encrypt):
        yaml_dict=self.file.file_to_dict() or {}
        
        if encrypt:
            value=self.encryption_class.encrypt_value(value=value)

        if obj in yaml_dict:
            inner_keys=yaml_dict[obj] 
        else:
            inner_keys={key:''}

        inner_keys[key]=value
        yaml_dict[obj]=inner_keys

        with open(self.config_filepath, 'w') as c_file:
            yaml.dump(yaml_dict, c_file)