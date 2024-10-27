import subprocess

from .logs import logger


def homebrew_install():
    """Installing Homebrew on Linux/MocOS systems."""

    try:
        subprocess.run(
            [
                "/bin/bash", "-c",
                "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in Homebrew installing: \n{err}")
        return False
    logger.info("Homebrew successfully installed.")


def homebrew_check():
    """Checking Homebrew in system on Linux/MacOS."""

    try:
        is_homebrew = subprocess.run(
            [
                'brew', '--version'
            ],
            capture_output=True,
            text=True,
            check=True
        )
    except Exception as err:
        logger.error(f"Something went wrong in checking Brew installation: \n{err}")
        return False
    finally:
        logger.info("Homebrew already installed in system.")
    return True
