import os
import re
from cryptography.fernet import Fernet


class Encryption():
    def __init__(self, key_directory, key_file):
        self.key_directory = key_directory
        self.key_path = f"{key_directory}/{key_file}"


    def check_for_directory(self):
        if os.path.isdir(self.key_directory) is False:
            os.makedirs(self.key_directory)


    def check_for_file(self):
        self.check_for_directory()
        print("here")
        print(os.path.exists(self.key_path))
        if os.path.exists(self.key_path) is False:
            self.generate_key()


    def generate_key(self):
        configer_key = Fernet.generate_key()
        with open(self.key_path, "wb") as key_f:
            key_f.write(configer_key)


    def load_key(self):
        return open(self.key_path, 'rb').read()


    def encrypt(self, value):
        key = self.load_key()
        encoded_value = value.encode()
        fernet = Fernet(key)
        encrypted_value = fernet.encrypt(encoded_value)
        return encrypted_value


    def encrypt_value(self, value):
        self.check_for_file()
        encrypted_value = self.encrypt(value=value).decode()
        return encrypted_value


    def decrypt(self, encrypted_value):
        key = self.load_key()
        fernet = Fernet(key)
        value = encrypted_value.encode()
        decrypted_pw = fernet.decrypt(value).decode()
        return decrypted_pw


    def decrypt_value(self, value):
        decrypted_value = self.decrypt(value)
        return decrypted_value