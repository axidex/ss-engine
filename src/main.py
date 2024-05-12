from fastapi import FastAPI

import urllib3

from src.api.apps import app_func, get_serv_app
from src.utils.endpoints import list_routes


def create_app():
    urllib3.disable_warnings()

    app = FastAPI()

    app.mount("/api", app_func)
    app.mount("/serv", get_serv_app(app_func))

    list_routes(app)

    return app

app = create_app()