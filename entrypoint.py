import uvicorn
import logging
import argparse
import os

from pytz import timezone

import src.configs.config as config
from src.metrics.check_health import check_health
from src.utils.logger import set_up_logging

TZ = timezone('Europe/Moscow')
NAME = "ss-engine"

if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--debug", action="store_true")
    args = argparser.parse_args()

    loglevel = logging.DEBUG if args.debug else logging.INFO
    if not args.debug:
        check_health()

    logpath = f"{os.path.join(config.logpath, NAME)}.log"

    set_up_logging(level=loglevel, tz=TZ, path=logpath)

    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=config.app_port,
        reload=True,
        log_config="log.ini" if not args.debug else "log.debug.ini",
        log_level=loglevel,
    )
