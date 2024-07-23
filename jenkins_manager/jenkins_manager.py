import click

from .utils import install_jenkins, delete_jenkins, verify_users, \
    create_guest, create_user


@click.group()
def cli():
    pass


@cli.command()
def install():
    """
    Install LTS version of Jenkins with dependencies.
    """
    install_jenkins()


@cli.command()
def create_users():
    """
    Create users in Jenkins (default: user, guest).
    """
    pass


@cli.command()
def verify():
    """
    Verifying security policy.
    """
    verify_users()


@cli.command()
def uninstall():
    """
    Uninstall Jenkins with files. 
    """
    delete_jenkins()
