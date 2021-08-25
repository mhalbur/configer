from .encryption import Encryption
from .file import File
from .read import Read
from .write import Write

"""
To Do:

Now that configuration is set up - need to update below code to get key paths and config file paths from easyfig's
config file

"""
class Config():
    def __init__(self, 
                 obj=None,
                 key=None,
                 value=None,
                 encrypt=False,
                 decrypt=False,
                 encryption_directory="/home/mroberts", 
                 encryption_file=".configer_secret",
                 configer_directory='configuration', 
                 configer_file='configer.yaml'):
        self.obj=obj
        self.key=key
        self.value=value
        self.encrypt=encrypt
        self.decrypt=decrypt
        self.encryption=Encryption(key_directory=encryption_directory, key_file=encryption_file)
        self.file=File(configer_directory=configer_directory, configer_file=configer_file)


    def set_value(self):
        Write(encryption=self.encryption, file=self.file).set_value(obj=self.obj, key=self.key, value=self.value, encrypt=self.encrypt)

    def get_value(self):
        Read(encryption_class=self.encryption, file_class=self.file).get_value(obj=self.obj, key=self.key, decrypt=self.decrypt)
