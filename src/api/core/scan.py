import logging
import os
import json
import shutil

from fastapi import HTTPException

from src.configs import config

from src.api.core.helper import Helper

from src.tools.deepsecrets.cmd import ds_launch_async
from src.tools.gitleaks.cmd import gl_launch_async

from src.mapping.ss_servicer import SSServicer

from src.api.core.send_to_db import send_to_db, update_task_status, get_task

logger = logging.getLogger(__name__)


async def start_scan_async(unpacked_size: int, cur_path: str, cur_id: str):

    task = None

    try:
        Helper.engine_start(cur_id)
        task = await get_task(cur_id)
        await update_task_status(1, task)

        gl_return_code, ds_return_code = -1, -1

        scanners_status_codes = []

        gl_report_path = os.path.join(cur_path, f"{cur_id}_gl.json")
        gl_return_code = await gl_launch_async(config.gl_path, cur_path, gl_report_path, config.gl_args, config.gl_timeout)
        scanners_status_codes.append(gl_return_code)
        logger.info(f"Return code - {gl_return_code=} | {cur_id}")

        if unpacked_size < Helper.max_file_size_ds:
            ds_report_path = os.path.join(cur_path, f"{cur_id}_ds.json")
            ds_return_code = await ds_launch_async(config.ds_path, cur_path, ds_report_path, config.ds_args, config.ds_timeout)
            scanners_status_codes.append(ds_return_code)
            logger.info(f"Return code - {ds_return_code=} | {cur_id}")

        if all((code != 0 for code in scanners_status_codes)):
            raise HTTPException(400, detail="Scan Failed")

        logger.info("Scan Finished -> Now Parsing")

        logger.info("Reading files")
        reports = list()
        if gl_return_code == 0:
            with open(gl_report_path, "r") as f:
                reports.append(
                    {"scanResult": json.load(f), "practiceTool": "gitleaks"}
                )
        if ds_return_code == 0:
            with open(ds_report_path, "r") as f:
                reports.append(
                    {"scanResult": json.load(f), "practiceTool": "deepsecrets"}
                )

        prefixes_to_remove = [
            os.path.join(prefix, cur_id) for prefix in config.prefixes_to_remove
        ]

        logger.info(f"Start parsing...")
        servicer = SSServicer(prefixes_to_remove)
        report = servicer.start(reports)
        logger.info("Report generated")
        await send_to_db(report, task)
        logger.info(f"Task {task.task_ss_pk} updated with results")

    except Exception as e:
        if task:
            await update_task_status(2, task)
            logger.exception(f"Task {task.task_ss_pk} failed | {e}")

        raise e
    finally:
        shutil.rmtree(cur_path)
        Helper.engine_stop()

