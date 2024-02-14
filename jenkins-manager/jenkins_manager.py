import click

from utils import install_jenkins, delete_jenkins, verify_users, \
    create_guest, create_user


@click.command()
def install():
    install_jenkins()


@click.command()
def create_users():
    pass


@click.command()
def verify():
    verify_users()


@click.command()
def uninstall():
    delete_jenkins()
