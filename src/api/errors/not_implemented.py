from fastapi import Request
from fastapi.responses import JSONResponse

import logging

logger = logging.getLogger(__name__)


async def not_implemented_exception_handler(request: Request, exc: NotImplementedError):
    status = "Not implemented yet"
    logger.error(status)

    return JSONResponse(
        status_code=501,
        content={
            "details": status
        }
    )