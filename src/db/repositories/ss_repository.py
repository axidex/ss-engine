from src.db.abc.repository import Repository

from src.db.schemas.client import Client
from src.db.schemas.task_ss import TaskSS


class SSRepository(Repository):
    """"""

    async def get_task(self, task_id: str) -> TaskSS | None:
        """"""

        return await self.db_client.get_task(task_id)

    async def create_task(self, task_id: str, client_id: int) -> TaskSS:
        """"""

        return await self.db_client.create_task(task_id, client_id)

    async def update_status(self, status: int, task: TaskSS) -> None:
        """"""

        return await self.db_client.update_status(status, task)

    async def send_report(self, report: dict, task: TaskSS) -> None:
        """"""

        return await self.db_client.send_report(report, task)

    async def get_client(self, cn: str) -> Client | None:
        """"""

        return await self.db_client.get_client(cn)

    async def create_client(self, cn: str) -> Client:
        """"""

        return await self.db_client.create_client(cn)
