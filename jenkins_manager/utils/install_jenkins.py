import distro

import platform
import subprocess

from .logs import logger
from .install_java import check_java
from .install_brew import homebrew_install, homebrew_check
from .settings import DEB_DISTRO, RHL_DISTRO, \
    JENKINS_GPG, LTS_JENKINS_RPM_KEY, LTS_JENKINS_RPM_REPO, LTS_JENKINS_RPM_KEYRINGS_PATH, \
    LTS_JENKINS_DEB_KEY, LTS_JENKINS_DEB_KEYRINGS_PATH, LTS_JENKINS_DEB_BINARY


def install_jenkins(mode: str="lts") -> bool:
    """Checking Host OS and running function for installing Jenkins with specified mode."""

    os_name = platform.system()
    if os_name == "Linux":
        if check_java(os_name):
            install_jenkins_linux(mode)
            return True
        print("Jenkins require installation Java version 8, 11, 12. Please install Java.")
        logger.error(
            "Java is not installed in system."
        )
        return False

    if os_name == "OSX":
        osx_jenkins_installation(mode)

    if os_name == "Windows":
        windows_jenkins_installation(mode)
        return False


def install_jenkins_linux(release: str):
    """Checking Linux distro. [Debian-based, RHL-based]"""

    distr = distro.id()

    if distr in DEB_DISTRO:
        debian_jenkins_installation(release)

    if distr in RHL_DISTRO:
        rhl_jenkins_installation(release)


def debian_jenkins_installation(release: str) -> bool:
    """Installing Jenkins in Debian-based systems. This function following next steps:
    1) Getting the Repo address;
    2) Adding the Repo key;
    3) Updating Repo list;
    4) Installing Jenkins."""

    try:
        subprocess.run(
            [
                "sudo", "wget", "-O", LTS_JENKINS_DEB_KEYRINGS_PATH,
                LTS_JENKINS_DEB_KEY,
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong: \n{err}")
        return False
    logger.info("Jenkins keyring added.")

    try:
        subprocess.run(
            [
                "sudo", "deb", f"[signed-by={LTS_JENKINS_DEB_KEYRINGS_PATH}]",
                LTS_JENKINS_DEB_BINARY, '|', "sudo", "tee", JENKINS_GPG,
                '>', "/dev/null",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong: \n{err}")
        return False
    logger.info("Jenkins repo added.")

    try:
        subprocess.run(
            [
                "sudo", "apt", "update",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong: \n{err}")
        return False
    logger.info("Repo list updated.")

    try:
        subprocess.run(
            [
                "sudo", "apt", "install", "jenkins",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong: \n{err}")
        return False
    logger.info("Jenkins installed")

    return True
    

def rhl_jenkins_installation(release: str) -> bool:
    """Installing Jenkins with in systems with supporting 'yum' package manager.
        This function following next steps:
        1) Getting the Repo address;
        2) Adding the Repo key;
        3) Updating Repo list;
        4) Installing dependencies;
        5) Installing Jenkins."""

    try:
        subprocess.run(
            [
                "sudo", "wget", "-O", LTS_JENKINS_RPM_KEYRINGS_PATH,
                LTS_JENKINS_RPM_REPO,
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in repo adding: \n{err}")
        return False
    logger.info("Jenkins repo added.")

    try:
        subprocess.run(
            [
                "sudo", "rpm", "--import", LTS_JENKINS_RPM_KEY
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in key adding: \n{err}")
        return False
    logger.info("Jenkins keys added.")

    try:
        subprocess.run(
            [
                "sudo", "yum", "update",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in repository update: \n{err}")
        return False
    logger.info("Repositories list updated.")

    try:
        subprocess.run(
            [
                "sudo", "yum", "install", "fontconfig", "java-17-openjdk",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in installing additional tools: \n{err}")
        return False
    logger.info("Repo list updated.")

    try:
        subprocess.run(
            [
                "sudo", "yum", "install", "jenkins",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in Jenkins installation: \n{err}")
        return False
    logger.info("Jenkins has been installed.")

    try:
        subprocess.run(
            [
                "sudo", "systemctl", "daemon-reload",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in daemons reloading: \n{err}")
        return False
    logger.info("Daemons successfully reloaded.")

    return True


def windows_jenkins_installation(release: str) -> bool:
    return False


def osx_jenkins_installation(release: str) -> bool:
    """Installing Jenkins in MacOS systems and checking Homebrew installation."""

    is_homebrew = homebrew_check()
    if not is_homebrew:
        logger.error("Homebrew is not installed.")
        homebrew_yn = str(input("Do you want to install Homebrew? (yes/no)"))
        if homebrew_yn.lower() == "yes":
            homebrew_install()

    try:
        subprocess.run(
            [
                "brew", "install", "jenkins-lts",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in Jenkins installing: \n{err}")
        return False
    logger.info("Jenkins successfully installed.")

    try:
        subprocess.run(
            [
                "brew", "services", "start", "jenkins-lts",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in Jenkins running: \n{err}")
        return False
    logger.info("Jenkins services successfully running.")

    return True
