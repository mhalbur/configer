from .main import Config

def set_value(obj, key, value, encrypt=False, config_file=None, **args):
    Config(config_file).set_value(obj, key, value, encrypt, **args)


def get_value(obj, key, decrypt=False, config_file=None, **args):
    value = Config(config_file).get_value(obj, key, decrypt, **args)
    return value
