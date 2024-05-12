import logging

from src.tools.create_process import run

logger = logging.getLogger(__name__)


def gl_check_cmd():
    cmd = [
        "--help"
    ]

    return cmd


async def gl_check_async(scanner_path: str, timeout=60):
    cmd = gl_check_cmd()
    logger.info(f"GL_LAUNCH_ARGS: {cmd} | GL_SCANNER_PATH: {scanner_path}")

    return await run(scanner_path, cmd, timeout, logger)
