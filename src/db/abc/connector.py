from abc import ABC, abstractmethod

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession


class Connector(ABC):
    """"""

    @property
    @abstractmethod
    def get_session(self) -> sessionmaker[AsyncSession]:
        """"""