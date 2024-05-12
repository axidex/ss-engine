from src.configs.config import postgres_config

from src.db.connectors.postgres_connector import PostgresConnector
from src.db.clients.postgres_client import PostgresClient
from src.db.repositories.ss_repository import SSRepository

from src.db.schemas.task_ss import TaskSS

ss_repository = SSRepository(
    db_client=PostgresClient(
        connector=PostgresConnector(
            db_url=f"postgresql+asyncpg://{postgres_config.username}:{postgres_config.password}@{postgres_config.host}:{postgres_config.port}/{postgres_config.database}"
        )
    )
)


async def send_to_db(report: dict, task: TaskSS) -> None:
    await ss_repository.send_report(report, task)


async def update_task_status(status: int, task: TaskSS) -> None:
    await ss_repository.update_status(status, task)


async def create_task(task_id: str, cn: str) -> TaskSS:
    client = await ss_repository.get_client(cn)
    if not client:
        client = await ss_repository.create_client(cn)
    return await ss_repository.create_task(task_id, client.client)


async def get_task(task_id: str) -> TaskSS:
    return await ss_repository.get_task(task_id)
