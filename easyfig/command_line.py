import click
import getopt
import re
import sys
from easyfig.main import Config
from easyfig.configuration import EasyConfig_Config


@click.group()
def main():
   pass


@click.command()
@click.option('--name', help="Name of the vendor/object (ie: snowflake, google, databricks, aws)")
@click.option('--key', help="Name of the key (ie: username, password, access_key)")
@click.option('--value', help="Value of the key (ie: What your username is, what your password is, what your access_key is)")
@click.option('--config_file', default=None)
@click.option('--encrypt', default=False)
def setvalue(name, key, value, encrypt, config_file):
    Config(config_file=config_file).set_value(obj=name, key=key, value=value, encrypt=encrypt)


@click.command()
@click.option('--name', help="Name of the vendor/object (ie: snowflake, google, databricks, aws)")
@click.option('--key', help="Name of the key (ie: username, password, access_key)")
@click.option('--config_file', default=None)
@click.option('--decrypt', default=False)
def getvalue(name, key, decrypt, config_file):
    value = Config(config_file=config_file).get_value(obj=name, key=key, decrypt=decrypt)
    click.echo(value)


@click.command()
@click.option('--filepath', default=None)
@click.option('--config_file', default=None)
def projectconfiger(filepath):
    config_path = EasyConfig_Config().create_project_config(filepath=filepath)
    click.echo(f"Created project configuration file at {config_path}.")


@click.command()
def setup():
    EasyConfig_Config().setup()


main.add_command(setvalue)
main.add_command(getvalue)
main.add_command(projectconfiger)
main.add_command(setup)
