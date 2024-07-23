import logging


def logger_config():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler("jenkins-manager.log")
        ]
    )

    logger = logging.getLogger(__name__)
    return logger


logger = logger_config()
