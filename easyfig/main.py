import sys
from .encryption import Encryption
from .file import File
from .read import Read
from .write import Write
from .configuration import EasyConfig_Config


class Config():
    def __init__(self):
        self.project_config = EasyConfig_Config().get_project_path()
        self.encryption_path = EasyConfig_Config().get_key_path()
        self.encryption=Encryption(encryption_config=self.encryption_path)
        self.file=File(project_config=self.project_config)


    def checker(self):
        if self.project_config == 'exit' or self.encryption_path=='exit':
            sys.exit()


    def set_value(self, obj, key, value, encrypt=False):
        self.checker()
        Write(encryption=self.encryption, file=self.file).set_value(obj=obj, key=key, value=value, encrypt=encrypt)


    def get_value(self, obj, key, decrypt=False):
        self.checker()
        Read(encryption_class=self.encryption, file_class=self.file).get_value(obj=obj, key=key, decrypt=decrypt)


    def view_file(self):
        self.checker()
        Read(encryption_class=self.encryption, file_class=self.file).view_file()
