from fastapi import APIRouter, File, HTTPException, UploadFile, BackgroundTasks
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from typing import Annotated

from src.tools.deepsecrets.check_health import ds_check_async
from src.tools.gitleaks.check_health import gl_check_async

from src.utils.archive import get_archive_contents_size, convert_size

from src.configs import config
from src.api.core.helper import Helper

from src.api.core.scan import start_scan_async

import logging
import os
import zipfile


logger = logging.getLogger(__name__)

router = APIRouter(prefix="/v1")

@router.post(
    "/SS",
    tags=["SS"],
    summary="Upload File and get ss Results",
    description="Perform SS",
)
async def ss_endpoint(
        zip_model: Annotated[
            UploadFile,
            File(description=f"Zip file | max File Size = {convert_size(Helper.max_file_size)}"),
        ],
        task_id: str,
        background_tasks: BackgroundTasks,
):
    """
    Performing SS

    :param zip_model:
    :param task_id:
    :param background_tasks:
    :return JSONResponse:
    """

    if Helper.working:
        raise HTTPException(400, detail="Engine is busy")

    cur_id = task_id

    Helper.engine_start(cur_id)
    try:
        if any(
                (
                    zip_model.content_type not in ("application/zip", "application/octet-stream"),
                    zip_model.filename.split(".")[-1] != "zip",
                    not zipfile.is_zipfile(zip_model.file),
                )
        ):
            logger.info(f"Invalid file type {zip_model.content_type}")
            raise HTTPException(400, detail=f"Invalid file type, got {zip_model.content_type}")

        file = zip_model.file

        unpacked_size = get_archive_contents_size(file, Helper.max_file_size)
        logger.info(f"Archive size {convert_size(zip_model.size)}")
        if unpacked_size < 0:
            logger.error("Max file size exceeded")
            raise HTTPException(500, detail="File Too Large")
        logger.info(f"Unpacked size {convert_size(unpacked_size)}")

        cur_path = os.path.join(config.tmp_path, str(cur_id))
        logger.info(f"Trying to create tmp folder: {cur_path}")
        os.makedirs(cur_path, exist_ok=True)
        logger.info("Folder created")

    except Exception as e:
        logger.exception(f"Preprocessed failed | {e}")
        Helper.engine_stop()

    else:
        background_tasks.add_task(start_scan_async, unpacked_size, cur_path, cur_id)

    return JSONResponse(content=jsonable_encoder({"taskId": cur_id}))

@router.get("/check-health", tags=["SS"])
async def ss_check_health():
    if Helper.working:
        return JSONResponse(
            content=jsonable_encoder({"status": f"{Helper.task_id}"}),
            status_code=400
        )

    ds_return_code = await ds_check_async(config.ds_path)
    gl_return_code = await gl_check_async(config.gl_path)

    if ds_return_code != 0 and gl_return_code != 0:
        logger.warning(f"Tools aren't healthy")
        return JSONResponse(content=jsonable_encoder({"status": "Not Ready"}))
    logger.info("Tools are healthy")

    return JSONResponse(content=jsonable_encoder({"status": "Ready"}))



