import argparse
import click

from utils import install_jenkins, delete_jenkins


@click.command()
def install():
    install_jenkins()


@click.command()
def create_users():
    pass


@click.command()
def verify():
    pass


@click.command()
def uninstall():
    delete_jenkins()
