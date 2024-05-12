import os
import logging

from src.tools.create_process import run

logger = logging.getLogger(__name__)


def ds_cmd(src_path: str, report_file: str, args: list[str]):
    cmd = [
        "--target-dir",
        f"{src_path}"
        "--outfile",
        f"{report_file}"
    ]

    if args:
        cmd.extend(args)
    return cmd


async def ds_launch_async(scanner_path: str, src_path: str, report_file: str, args=None, timeout=60):
    if args is None:
        args = []

    os.makedirs(os.path.dirname(report_file), exist_ok=True)

    cmd = ds_cmd(src_path, report_file, args)
    logger.info(f"GL_LAUNCH_ARGS: {cmd} | GL_SCANNER_PATH: {scanner_path}")

    return await run(scanner_path, cmd, timeout, logger)