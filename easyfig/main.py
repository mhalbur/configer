import sys
from .encryption import Encryption
from .file import File
from .read import Read
from .write import Write
from .configuration import EasyConfig_Config


class Config():
    def __init__(self, config_file=None):
        self.encryption_path = EasyConfig_Config().get_key_path()
        self.encryption=Encryption(encryption_config=self.encryption_path)
        
        self.file=File(config_file=config_file)
        self.config_file = self.file.config_file
        self.config_filepath = self.file.config_filepath

    def checker(self):
        if self.config_file == 'exit' or self.encryption_path=='exit':
            sys.exit()

    def set_value(self, obj, key, value, encrypt=False):
        self.checker()
        Write(encryption=self.encryption, config_file=self.config_file).set_value(obj=obj, key=key, value=value, encrypt=encrypt)

    def get_value(self, obj, key, decrypt):
        self.checker()
        value = Read(encryption_class=self.encryption, config_file=self.config_file).get_value(obj=obj, key=key, decrypt=decrypt)
        return value

    def view_file(self):
        self.checker()
        Read(encryption_class=self.encryption, file_class=self.config_file).view_file()
