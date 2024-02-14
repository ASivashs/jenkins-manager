from pathlib import Path

from .logs import logger
from .settings import diriterdir


def verify_users(users: list | set | tuple=("admin", "user", "guest")):
    dir = Path("/var/lib/jenkins/users")
    verified_users = []
    for entry in diriterdir:
        if current_user:=str(entry).lower().split("_")[0] in users:
            logger.info(f"User {current_user} exist and verified.")
            verified_users.append(current_user)
        else:
            logger.warning(f"User {current_user} does not exist.")
    if verified_users == users:
        logger.info("Verified successfully, all secure politics in good condition.")
    else:
        logger.warning("Verified successfully, some users does not exist.")
