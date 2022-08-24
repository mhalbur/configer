from .main import Config

def set_value(obj, key, value, **args):
    Config(obj, key, value, **args).set_value()


def get_value(obj, key, decrypt=False, **args):
    value = Config().get_value(obj, key, decrypt, **args)
    return value
