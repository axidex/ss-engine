import time
import logging
import requests

logger = logging.getLogger(__name__)

def check_health():
    while True:
        try:
            response = requests.head("http://localhost:15021/healthz/ready")
            if response.status_code == 200:
                break

        except requests.exceptions.RequestException:
            pass

        logger.info(".", end="", flush=True)

        time.sleep(1)

    with open("/tmp/liveness-check/check", "w") as file:
        file.write("ready")

    logger.info("Service is ready to start")