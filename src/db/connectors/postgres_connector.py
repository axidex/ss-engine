from src.db.abc.connector import Connector

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

class PostgresConnector(Connector):

    def __init__(self, db_url: str):

        self.engine = create_async_engine(db_url, echo=False)
        self.session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False,
        )

    @property
    def get_session(self) -> sessionmaker[AsyncSession]:
        """"""

        return self.session
    