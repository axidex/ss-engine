from abc import ABC

from src.db.abc.db_client import DBClient


class Repository(ABC):
    """"""

    def __init__(self, db_client: DBClient):
        """"""

        self.db_client = db_client