import os
import logging

from datetime import datetime


def set_up_logging(level: str, tz=None, path: str = None):
    if tz:
        def timetz(*args):
            return datetime.now(tz=tz).timetuple()

        logging.Formatter.converter = timetz

    handlers = [logging.StreamHandler()]

    if path:
        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok=True)
        handlers.append(logging.FileHandler(path))

    logging.basicConfig(
        level=level,
        format="[%(asctime)s.%(msecs)03d] %(levelname)s - %(name)s:%(message)s",
        handlers=handlers,
    )
