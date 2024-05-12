from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from src.api.routes import get_v1_router

import src.api.errors as exception_handlers


def get_func_app() -> FastAPI:

    app_func = FastAPI(
        title= "SS API",
        description= "API for SS",
        version="1.0.0",
    )

    app_func.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Auxiliary
    app_func.add_exception_handler(Exception, exception_handlers.exception_handler)
    app_func.add_exception_handler(NotImplementedError, exception_handlers.not_implemented_exception_handler)

    app_func.include_router(get_v1_router())

    return app_func
