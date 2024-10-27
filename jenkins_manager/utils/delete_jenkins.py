import distro

import platform
import subprocess

from .install_brew import homebrew_check
from .logs import logger
from .settings import DEB_DISTRO, RHL_DISTRO, ARCH_DISTRO, SUSE_DISTRO


def remove_jenkins():
    """Checking Host OS and running function for removing Jenkins with specified mode."""

    os_name = platform.system()

    if os_name == "Linux":
        distr = distro.id()

        if distr in DEB_DISTRO:
            remove_deb_jenkins()

        if distr in RHL_DISTRO:
            remove_rhl_jenkins()

    if os_name == "Windows":
        remove_windows_jenkins()

    if os_name == "OSX":
        remove_osx_jenkins()


def remove_deb_jenkins() -> bool:
    """Removing Jenkins in Debian-based systems. This function following next steps:
        1) Remove Jenkins package;
        2) Removing Jenkins dependencies."""

    try:
        subprocess.run(
            [
                "sudo", "apt-get", "remove", "--purge", "-y", "jenkins",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in removing Jenkins: {err}")
        return False
    logger.info("Jenkins uninstalled.")

    try:
        subprocess.run(
            [
                "sudo", "rm", "-rf", "/var/lib/jenkins",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong: {err}")
        return False
    logger.info("Jenkins directory removed.")

    return True


def remove_rhl_jenkins() -> bool:
    """Removing Jenkins in RHL-based systems. This function following next steps:
            1) Remove Jenkins package;
            2) Removing Jenkins dependencies."""

    try:
        subprocess.run(
            [
                "sudo", "yum", "-y", "jenkins",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in removing Jenkins: {err}")
        return False
    logger.info("Jenkins uninstalled.")

    try:
        subprocess.run(
            [
                "sudo", "rm", "-rf", "/var/lib/jenkins",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in removing Jenkins dependencies: {err}")
        return False
    logger.info("Jenkins directory removed.")

    return True


def remove_osx_jenkins():
    """Removing Jenkins in MacOS systems."""

    is_homebrew = homebrew_check()

    if not is_homebrew:
        logger.error("Cannot remove Jenkins: Homebrew is not installed in system.")
        print("Cannot remove Jenkins, because this system dont contain Homebrew.")
        return False

    if is_homebrew:
        try:
            subprocess.run(
                [
                    "brew", "uninstall", "jenkins-lts", "jenkins",
                ]
            )
        except Exception as err:
            logger.error(f"Something went wrong in removing Jenkins: {err}")
            return False
        logger.info("Jenkins uninstalled.")


def remove_windows_jenkins():
    pass
