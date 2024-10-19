import distro

import subprocess

from .logs import logger
from .settings import DEB_DISTRO, RPM_DISTRO


def check_java(os_name: str) -> bool:
    if os_name == "Linux":
        java_path = subprocess.check_output(["which", "java"])
        if java_path:
            logger.info("Java already installed in the system.")
            return True

        if not java_path:
            logger.warning("Missing Java package. Please install Java in your system.")
            java_yn = str(input("Do you want to install java? (yes/no)"))
            if java_yn.lower() == "yes":
                install_java(os_name)

    if os_name == "Windows":
        return False
        # install_java(os_name)

    return False


def install_java(os_name: str):
    if os_name == "Linux":
        distr = distro.id()

        if distr in DEB_DISTRO:
            try:
                subprocess.run(
                    [
                        "sudo",
                        "apt",
                        "update",
                    ]
                )
            except Exception as err:
                logger.error(f"Something went wrong: {err}")
                return False
            logger.info("Repositories list updated.")
            try:
                subprocess.run(
                    [
                        "sudo",
                        "apt",
                        "install",
                        "default-jre",
                    ]
                )
            except Exception as err:
                logger.error(f"Something went wrong: {err}")
                return False
            logger.info("JRE installed.")
            try:
                subprocess.run(
                    [
                        "sudo",
                        "apt",
                        "install",
                        "default-jdk",
                    ]
                )
            except Exception as err:
                logger.error(f"Something went wrong: {err}")
                return False
            logger.info("JDK installed.")

        if distr in RPM_DISTRO:
            pass

        return check_java()

    if os_name == "Windows":
        pass
