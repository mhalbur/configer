from .config import Config

def set_value(obj, key, value, **args):
    Config(obj, key, value, **args).set_value()


def get_value(obj, key, **args):
    Config(obj, key, **args).get_value()

