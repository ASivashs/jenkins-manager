import distro

import platform
import subprocess

from .logs import logger
from .install_java import check_java
from .settings import DEB_DISTRO, RHL_DISTRO, \
    JENKINS_GPG, LTS_JENKINS_RPM_KEY, LTS_JENKINS_RPM_REPO, LTS_JENKINS_RPM_KEYRINGS_PATH, \
    LTS_JENKINS_DEB_KEY, LTS_JENKINS_DEB_KEYRINGS_PATH, LTS_JENKINS_DEB_BINARY


def install_jenkins(mode: str="lts") -> bool:
    os_name = platform.system()
    if os_name == "Linux":
        if check_java(os_name):
            install_jenkins_linux(mode)
            return True
        logger.error(
            "Jenkins require installation Java version 8, 11, 12. Please install Java."
        )
        return False

    if os_name == "OSX":
        osx_jenkins_installation(mode)

    if os_name == "Windows":
        windows_jenkins_installation(mode)
        return False


def install_jenkins_linux(release: str="lts"):
    distr = distro.id()

    if distr in DEB_DISTRO:
        debian_jenkins_installation(release)

    if distr in RHL_DISTRO:
        rhl_jenkins_installation(release)


def debian_jenkins_installation(release: str="lts") -> bool:
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
    

def rhl_jenkins_installation(release: str="lts") -> bool:
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


def windows_jenkins_installation(release: str="lts"):
    pass


def osx_jenkins_installation(release: str="lts"):
    pass
