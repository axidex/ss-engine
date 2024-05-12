from src.db.abc.connector import Connector

from abc import ABC, abstractmethod

from src.db.schemas.task_ss import TaskSS
from src.db.schemas.client import Client


class DBClient(ABC):
    """"""

    def __init__(self, connector: Connector):
        """"""

        self.connector = connector

    @abstractmethod
    async def get_task(self, task_id: str) -> TaskSS | None:
        """"""

    @abstractmethod
    async def create_task(self, task_id: str, client_id: int) -> TaskSS:
        """"""

    @abstractmethod
    async def update_status(self, status: int, task: TaskSS) -> None:
        """"""

    @abstractmethod
    async def send_report(self, report: dict, task: TaskSS) -> None:
        """"""

    @abstractmethod
    async def get_client(self, cn: str) -> Client | None:
        """"""

    @abstractmethod
    async def create_client(self, cn: str) -> Client:
        """"""
