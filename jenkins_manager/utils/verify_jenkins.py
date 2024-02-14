from pathlib import Path

from .logs import logger
from .settings import diriterdir


def verify_users(users: list | set | tuple=("admin", "user", "guest")):
    dir = Path("/var/lib/jenkins/users")
    verified_users = []
    for entry in diriterdir:
        if entry in users:
            logger.info(f"User {entry} exist and verified.")
            verified_users.append(entry)
        else:
            logger.warning(f"User {entry} does not exist.")
    if verified_users == users:
        logger.info("Verified successfully, all secure politics in good condition.")
    else:
        logger.warning("Verified successfully, some users does not exist.")
