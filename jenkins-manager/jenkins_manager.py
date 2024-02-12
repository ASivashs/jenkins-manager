import argparse
import click

from utils import install_jenkins


@click.command()
@click.option(
    
)
def jenkins_install():
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-i", "--install", 
        help=""
    )
    parser.add_argument(
        "-s", "--start", 
        help="", 
        type=str, 
        default="JENKINS_PASSWORD=admin"
    )
    parser.add_argument(
        "-v", "--verify", 
        help=""
    )
    parser.add_argument(
        "-d", "--delete", 
        help=""
    )
    
    args = parser.parse_args()


if __name__ == "__main__":
    main()
