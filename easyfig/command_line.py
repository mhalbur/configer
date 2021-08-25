import click
from easyfig.main import Config
from easyfig.configuration import EasyConfig_Config


@click.group()
def main():
   pass


@click.command()
@click.argument('setvalue')
def setvalue(setvalue):
    split_variable=setvalue.split(":")
    Config(obj=split_variable[0], key=split_variable[1], value=split_variable[2]).set_value()


@click.command()
@click.argument('getvalue')
def getvalue(getvalue):
    split_variable=getvalue.split(":")
    value = Config(obj=split_variable[0], key=split_variable[1]).get_value()
    click.echo(value)


@click.command()
@click.option('--filepath', default=None)
def configer(filepath):
    config_path = EasyConfig_Config().create_repo_config(filepath=filepath)
    click.echo(f"Created repo configuration file at {config_path}.")


@click.command()
@click.option('--keypath', default=None)
def setup(keypath):
    EasyConfig_Config().setup(keypath=keypath)



main.add_command(setvalue)
main.add_command(getvalue)
main.add_command(configer)
main.add_command(setup)
