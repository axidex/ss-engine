from abc import ABC, abstractmethod

from src.dataclasses.secret_finding import SecretFinding


class Mapper(ABC):
    """Class for mapping results"""

    # Метод для дедубликации результатов
    @abstractmethod
    def match(self, reports: list[list[SecretFinding]]) -> list[SecretFinding]:
        """"""


    # Метод для деления не low, medium, high
    @abstractmethod
    def map(self, reports: list[list[SecretFinding]]) -> list[SecretFinding]:
        """"""