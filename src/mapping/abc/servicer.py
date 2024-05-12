from abc import ABC, abstractmethod

from typing import Iterable

from .parser import Parser
from .mapper import Mapper

from src.dataclasses.secret_finding import SecretFinding


class Servicer(ABC):
    """Class for performing report parsing and mapping"""

    def __init__(self):
        """"""

        self.mapper: Mapper
        self.parsers: dict[str, Parser]

    @abstractmethod
    def start(self, raw_reports: Iterable[dict]) -> dict[str, list[dict]]:
        """"""

    @abstractmethod
    def divide_reports(self, raw_reports: Iterable[dict]) -> list[list[SecretFinding]]:
        """"""

