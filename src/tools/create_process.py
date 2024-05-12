import asyncio
import subprocess
import psutil
import logging


async def run(scanner_path: str, cmd: list, timeout: int, logger: logging.Logger) -> int:
    """"""
    proc: asyncio.subprocess.Process = await create_process_async(scanner_path, cmd)

    try:
        stdout_task = asyncio.create_task(read_stream(proc.stdout, logger))
        stderr_task = asyncio.create_task(read_stream(proc.stderr, logger))

        await asyncio.wait([stdout_task, stderr_task])

        _ = await asyncio.wait_for(proc.communicate(), timeout=timeout)

    except asyncio.TimeoutError:
        if proc.returncode is None:
            parent = psutil.Process(proc.pid)
            for child in parent.children(recursive=True):
                child.terminate()
            parent.terminate()
            logger.warning(f"Terminating process {scanner_path=}, {cmd=} (timed out)")

        return proc.returncode if proc.returncode == 0 else 1337


async def create_process_async(scanner_path: str, cmd: list) -> asyncio.subprocess.Process:
    process = await asyncio.create_subprocess_exec(
        scanner_path,
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    )

    return process


def create_process(scanner_path: str, cmd: list) -> subprocess.CompletedProcess:
    process = subprocess.run(
        *[scanner_path].extend(cmd),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    )

    return process


async def read_stream(stream, logger: logging.Logger):
    while True:
        line = None
        if stream:
            line: bytes | None = await stream.readline()
        if line:
            logger.info(line.decode().strip())
        else:
            break
