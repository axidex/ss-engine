import logging

from src.tools.create_process import run

logger = logging.getLogger(__name__)


def ds_check_cmd():
    cmd = [
        "--help"
    ]

    return cmd


async def ds_check_async(scanner_path: str, timeout=60):
    cmd = ds_check_cmd()
    logger.info(f"GL_LAUNCH_ARGS: {cmd} | GL_SCANNER_PATH: {scanner_path}")

    return await run(scanner_path, cmd, timeout, logger)
