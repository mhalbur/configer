import click
import re
from easyfig.main import Config
from easyfig.configuration import EasyConfig_Config


@click.group()
def main():
   pass


@click.command()
@click.argument('setvalue')
@click.option('--encrypt', default=False)
def setvalue(setvalue, encrypt):
    r = r'(?<!\\)(?:\\\\)*\.'
    split_variable = [i.replace("\\", "") for i in re.split(r, setvalue)]
    Config().set_value(obj=split_variable[0], key=split_variable[1], value=split_variable[2], encrypt=encrypt)


@click.command()
@click.argument('getvalue')
def getvalue(getvalue):
    split_variable=getvalue.split(".")
    value = Config().get_value(obj=split_variable[0], key=split_variable[1])
    click.echo(value)


@click.command()
@click.option('--filepath', default=None)
def projectconfiger(filepath):
    config_path = EasyConfig_Config().create_project_config(filepath=filepath)
    click.echo(f"Created project configuration file at {config_path}.")


@click.command()
def setup():
    EasyConfig_Config().setup()


# make command for show file for project - is this actually needed though...?


main.add_command(setvalue)
main.add_command(getvalue)
main.add_command(projectconfiger)
main.add_command(setup)
