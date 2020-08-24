import base64
import os
import re
import yaml
from cryptography.fernet import Fernet


"""Make this into a class/add comments into functions"""


def check_for_key_file(key_directory, key_file):
    return os.path.isfile(f"{key_directory}/{key_file}")


def generate_key(key_directory, key_file):
    configer_key = Fernet.generate_key()
    with open(f"{key_directory}/{key_file}", "wb") as key_f:
        key_f.write(configer_key)


def load_key(key_directory, key_file):
    return open(f"{key_directory}/{key_file}", 'rb').read()


def encrypt(key_directory, key_file, value):
    key = load_key(key_directory=key_directory, key_file=key_file)
    encoded_value = value.encode()
    fernet = Fernet(key)
    encrypted_value = fernet.encrypt(encoded_value)

    return encrypted_value


def encrypt_value(value, key_directory, key_file):
    checker = check_for_key_file(key_directory=key_directory, key_file=key_file)

    if checker:
        encrypted_value = encrypt(key_directory=key_directory, key_file=key_file, value=value)
    else:
        generate_key(key_directory=key_directory, key=key)
        encrypted_value = encrypt(key_directory=key_directory, key_file=key_file, value=value)
    
    return encrypted_value


def set_value(key, value, key_directory="/home/mhalbur", key_file=".configer_secret", configer_directory='configuration', configer_file='configer.yaml'):
    """
        ToDo:
            -check if configer file exists
            -check if key exists in configer file
            -not overwrite the file
            -what's up with weird binary tag on encrypted value? 
            -need a better way to specify key_directory location - don't like spelling out user
    """
    if key in ["password", "pw", "pass"] or re.match('.*secret.*', key) or re.match('.*private.*', key) or re.match('.*key.*', key):
        value = encrypt_value(value=value, key_directory=key_directory, key_file=key_file)
    
    data={key:value}

    with open(f"{configer_directory}/{configer_file}", 'w') as c_file:
        yaml.dump(data, c_file)
