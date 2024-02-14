import distro

import platform
import subprocess

from .logs import logger
from .install_java import check_java
from .users import create_user, create_guest
from .settings import DEB_DISTRO, RPM_DISTRO, JENKINS_GPG, JENKINS_KEYRINGS_PATH, \
    LTS_JENKINS_BINARY, LTS_JENKINS_KEY


def install_jenkins() -> bool:
    os_name = platform.system()
    if os_name == "Linux":
        if check_java(os_name):
            installing_jenkins_linux("lts")
            return True
        logger.info(
            "Jenkins require installation Java version 8, 11, 12. Please install Java."
        )
        return False

    if os_name == "Windows":
        installing_windows()
        return False


def installing_jenkins_linux(release: str="lts") -> bool:
    """
    Specify jenkins version lts or weekly
    """
    distr = distro.id()
    if distr in DEB_DISTRO:
        try:
            subprocess.run(
                [
                    "sudo", "wget", "-O", JENKINS_KEYRINGS_PATH, \
                        LTS_JENKINS_KEY,
                ]
            )
        except Exception as err:
            logger.error(f"Something went wrong: {err}")
            return False
        logger.info("Jenkins keyring added.")
        try:
            subprocess.run(
                [
                    "sudo", "deb", f"[signed-by={JENKINS_KEYRINGS_PATH}]", \
                        LTS_JENKINS_BINARY, '|', "sudo", "tee", JENKINS_GPG, \
                            '>', "/dev/null",
                ]
            )
        except Exception as err:
            logger.error(f"Something went wrong: {err}")
            return False
        logger.info("Jenkins repo added.")
        try:
            subprocess.run(
                [
                    "sudo", "apt", "update",
                ]
            )
        except Exception as err:
            logger.error(f"Something went wrong: {err}")
            return False
        logger.info("Repo list updated.")
        try:
            subprocess.run(
                [
                    "sudo", "apt", "install", "jenkins",
                ]
            )
        except Exception as err:
            logger.error(f"Something went wrong: {err}")
            return False
        logger.info("Jenkins installed")
        
        try:
            subprocess.run(
                [
                    "sudo", "rm", "-rf", "/var/lib/jenkins/users",
                ]
            )
        except Exception as err:
            logger.error(f"Something went wrong: {err}")
            return False
        try:
            subprocess.run(
                [
                    "sudo", "cp", "-r", "users/", "/var/lib/jenkins/users",
                ]
            )
        except Exception as err:
            logger.error(f"Something went wrong: {err}")
            return False
        return True
    
    if distr in RPM_DISTRO:
        create_user()
        create_guest()
        return False


def installing_windows():
    pass


def installing_macos():
    pass
