import distro

import subprocess

from utils import logger
from utils import DEB_DISTRO, RPM_DISTRO

# from logs import logger
# from settings import DEB_DISTRO, RPM_DISTRO
    
    
def delete_jenkins() -> bool:
    distr = distro.id()
        
    if distr in DEB_DISTRO:
        try:
            subprocess.run(
                [
                    "sudo", "apt-get", "remove" "--purge", "-y", "jenkins",
                ]
            )
        except Exception as err:
            logger.error(f"Something went wrong: {err}")
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
    
    if distr in RPM_DISTRO:
        pass


if __name__ == "__main__":
    delete_jenkins()
