import base64
import os
from cryptography.fernet import Fernet


def check_for_key():
    # check for key
    # if exists = done
    # else generate key
    la = "check for key"


def load_key(directory, key):
    return open(f"{directory}/{key}", rb).read()


def generate_key(directory, key):
    # a good / secure place to store a key that won't get lost? 
    # configuruation is not a good place - but using it for testing
    key = Fernet.generate_key()
    with open(f"{directory}/{key}", "wb") as key_file:
        key_file.write(key)


def encrypt_value(directory="configuration", key="config_secret.key, value):
    check_for_key
    key = load_key()
    encoded_value = value.encode()
    f = Fernet(key)
    encrypted_value = f.encrypt(encoded_value)
