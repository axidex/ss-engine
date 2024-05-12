import logging
import os
import time

logger = logging.getLogger(__name__)


def wait_secret(path: str) -> None:
    while not os.path.exists(path):
        logger.info(f"Wait for secret [{path}]")
        time.sleep(5)

    logger.info(f"Secret [{path}] injected")