import distro

import platform
import subprocess

from .logs import logger
from .settings import DEB_DISTRO, RHL_DISTRO, ARCH_DISTRO, SUSE_DISTRO


def remove_jenkins():
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
    pass


def remove_windows_jenkins():
    pass
