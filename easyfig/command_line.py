import click
from easyfig.config import Config


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


main.add_command(setvalue)
main.add_command(getvalue)
