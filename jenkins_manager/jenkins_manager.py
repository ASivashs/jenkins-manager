import click

from .utils import install_jenkins, remove_jenkins


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--mode",
    default="lts",
    help="Type `lts` for long time support Jenkins version. If you want to "
         "install fresh version type `weekly`.",
)
def install(mode: str="lts"):
    """
    Install LTS or Weekly version of Jenkins with dependencies.
    """
    install_jenkins(mode)


@cli.command()
def uninstall():
    """
    Uninstall Jenkins with dependencies files.
    """
    remove_jenkins()
