from abc import ABC, abstractmethod

from src.dataclasses.secret_finding import SecretFinding


class Parser(ABC):
    """Class for uniforming Report"""

    def __init__(self, prefixes_to_remove=None):
        if prefixes_to_remove is None:
            prefixes_to_remove = []

        self.prefixes_to_remove = prefixes_to_remove

    @abstractmethod
    def process(self, report: dict) -> list[SecretFinding]:
        """"""
        