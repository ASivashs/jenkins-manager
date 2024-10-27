import distro

import subprocess
import shutil

from .logs import logger
from .settings import DEB_DISTRO, RHL_DISTRO, SUSE_DISTRO, ARCH_DISTRO


def check_java(os_name: str) -> bool:
    if os_name == "Linux":
        java_path = subprocess.check_output(
                [
                    "which", "java"
                ]
            )
        if java_path:
            logger.info("Java already installed in the system.")
            return True
        
        if not java_path:
            logger.warning(
                "Missing Java package. Please install Java in your system."
            )
            java_yn = str(input("Do you want to install java? (yes/no)"))
            if java_yn.lower() == "yes":
                install_java_linux()
                return True

    if os_name == "OSX":
        pass
    
    if os_name == "Windows":
        java_path = shutil.which("java")

        if java_path:
            logger.info("Java already installed in the system.")
            return True

        if not java_path:
            logger.warning(
                "Missing Java package. Please install Java in your system."
            )
            java_yn = str(input("Do you want to install java? (yes/no)"))
            if java_yn.lower() == "yes":
                # install_java_windows()
                return True
    return False


def install_java_linux():
    distr = distro.id()

    if distr in DEB_DISTRO:
        debian_java_installation()

    if distr in RHL_DISTRO:
        rhl_java_installation()

    if distr in SUSE_DISTRO:
        suse_java_installation()

    if distr in ARCH_DISTRO:
        arch_java_installation()


def debian_java_installation() -> bool:
    try:
        subprocess.run(
            [
                "sudo", "apt", "update",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in repository update: \n{err}")
        return False
    logger.info("Repositories list updated.")

    try:
        subprocess.run(
            [
                "sudo", "apt", "install", "default-jre",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in Debian JRE installation: \n{err}")
        return False
    logger.info("JRE installed.")

    try:
        subprocess.run(
            [
                "sudo", "apt", "install", "default-jdk",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in Debian JDK installation: \n{err}")
        return False
    logger.info("JDK installed.")

    return True


def rhl_java_installation() -> bool:
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
                "sudo", "yum", "install", "java"
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in java installation: \n{err}")
        return False
    logger.info("Java installed.")

    return True


def suse_java_installation() -> bool:
    try:
        subprocess.run(
            [
                "sudo", "zypper", "refresh",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in repository update: \n{err}")
        return False
    logger.info("Repositories list updated.")

    try:
        subprocess.run(
            [
                "sudo", "zypper", "install", "-y", "java-1_8_0-openjdk",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in java installation: \n{err}")
        return False
    logger.info("Java installed.")

    return True


def arch_java_installation() -> bool:
    try:
        subprocess.run(
            [
                "sudo", "pacman", "-Syu",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in repository update: \n{err}")
        return False
    logger.info("Repositories list updated.")

    try:
        subprocess.run(
            [
                "sudo", "pacman", "-S", "--noconfirm", "java-openjdk",
            ]
        )
    except Exception as err:
        logger.error(f"Something went wrong in java installation: \n{err}")
        return False
    logger.info("Java installed.")

    return True


def install_java_macos():
    pass


# def install_java_windows():
#     install_command = r'msiexec.exe /i "path\to\jenkins.msi" /qn /norestart INSTALLDIR="D:\Jenkins" JAVA_HOME="C:\Program Files\SomeJava" PORT=80 /L*v "path\to\logfile.txt"'
