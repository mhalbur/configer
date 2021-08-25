class Read():
    def __init__(self, encryption_class, file_class):
        self.encryption_class=encryption_class
        self.file_class=file_class

    def get_value(self, obj, key, decrypt):
        yaml_dict=self.file_class.file_to_dict()
        value=yaml_dict[obj][key]

        if decrypt:
            value=self.encryption_class.decrypt_value(value=value)
    
        print(value)
        return value
