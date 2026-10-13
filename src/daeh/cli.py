import click
from daeh.core.config import init_dirs
from daeh.commands import install, remove, list, search

@click.group()
@click.version_option()
def main():
    """Daeh - أداة إدارة حزم C بسيطة"""
    init_dirs()

main.add_command(install.install)
main.add_command(remove.remove)
main.add_command(list.list_packages)
main.add_command(search.search)
