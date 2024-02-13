from .main import Config

def set_value(obj, key, value, encrypt=False, **args):
    Config().set_value(obj, key, value, encrypt, **args)


def get_value(obj, key, decrypt=False, **args):
    value = Config().get_value(obj, key, decrypt, **args)
    return value
