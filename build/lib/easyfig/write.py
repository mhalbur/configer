import yaml

class Write():
    def __init__(self, encryption, file):
        self.encryption_class=encryption
        self.file_class=file

    def set_value(self, obj, key, value, encrypt):
        yaml_dict=self.file_class.file_to_dict() or {}
        
        if encrypt:
            value=self.encryption_class.encrypt_value(value=value)

        if obj in yaml_dict:
            inner_keys=yaml_dict[obj] 
        else:
            inner_keys={key:''}

        inner_keys[key]=value
        yaml_dict[obj]=inner_keys

        with open(self.file_class.project_config, 'w') as c_file:
            yaml.dump(yaml_dict, c_file)