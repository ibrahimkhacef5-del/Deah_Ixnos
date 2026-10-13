import click
from daeh.commands import install, remove, list_pkgs, search

@click.group()
@click.version_option()
def main():
    """Daeh - أداة إدارة حزم C بسيطة"""
    pass

main.add_command(install.install)
main.add_command(remove.remove)
main.add_command(list_pkgs.list_packages)
main.add_command(search.search)
