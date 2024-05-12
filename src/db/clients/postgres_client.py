from src.db.abc.db_client import DBClient

from sqlalchemy import select

from src.utils.retry import retry

from src.db.schemas.client import Client
from src.db.schemas.task_ss import  TaskSS


class PostgresClient(DBClient):
    """"""

    @retry(max_retries=5, timeout=0.01)
    async def get_task(self, task_id: str) -> TaskSS | None:
        """"""

        async with self.connector.get_session() as session:
            task = await session.execute(select(TaskSS).where(TaskSS.taskId == task_id))

        first = task.first()

        return first[0] if first else None

    @retry(max_retries=5, timeout=0.01)
    async def create_task(self, task_id: str, client_id: int) -> TaskSS:
        """"""

        task = TaskSS(client=client_id, taskId=task_id, status=1)

        async with self.connector.get_session() as session:
            session.add(task)
            await session.commit()

        return task


    @retry(max_retries=5, timeout=0.01)
    async def update_status(self, status: int, task: TaskSS) -> None:
        """"""

        async with self.connector.get_session() as session:
            task.status = status
            session.add(task)
            await session.commit()


    @retry(max_retries=5, timeout=0.01)
    async def send_report(self, report: dict, task: TaskSS) -> None:
        """"""

        async with self.connector.get_session() as session:
            task.status = 3
            task.result = report
            session.add(task)
            await session.commit()

    @retry(max_retries=5, timeout=0.01)
    async def get_client(self, cn: str) -> Client | None:
        """"""

        async with self.connector.get_session() as session:
            client = await session.execute(
                select(Client).where(Client.subject_name == cn)
            )
        first = client.first()

        return first[0] if first else None

    @retry(max_retries=5, timeout=0.01)
    async def create_client(self, cn: str) -> Client:
        """"""

        client = Client(subject_name=cn)

        async with self.connector.get_session() as session:
            session.add(client)
            session.commit()

        return client

