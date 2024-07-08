from .file import File

class Read():
    def __init__(self, encryption_class, config_file):
        self.encryption_class=encryption_class
        self.file=File(config_file)
        
        self.config_file = self.file.config_file
        self.config_filepath = self.file.config_filepath

    def get_value(self, obj, key, decrypt):
        yaml_dict=self.file.file_to_dict()
        value=yaml_dict[obj][key]
        if decrypt:
            value=self.encryption_class.decrypt_value(value=value)

        return value

    def view_file(self):
        with open(self.config_filepath, 'r') as c_file:
            for line in c_file:
                print(line)
