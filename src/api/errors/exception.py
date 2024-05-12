from fastapi import Request
from fastapi.responses import JSONResponse

import logging

logger = logging.getLogger(__name__)


async def exception_handler(request: Request, exc: NotImplementedError):

    logger.error(exc, stack_info=True)

    return JSONResponse(
        status_code=500,
        content={
            "details": "Not handled error"
        }
    )