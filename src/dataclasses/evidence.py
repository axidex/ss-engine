from enum import Enum


class Evidence(Enum):
    """Finding Evidence Level"""

    LOW = 1
    MEDIUM = 2
    HIGH = 3

    def __str__(self):
        return self.name.split(".")[-1]


e = {"HIGH": Evidence.HIGH, "MEDIUM": Evidence.MEDIUM, "LOW": Evidence.LOW}


def to_evidence(evidence_str: str) -> Evidence:
    """"""

    return e[evidence_str]
