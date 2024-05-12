from dataclasses import dataclass

from src.dataclasses.evidence import Evidence


@dataclass
class SecretFinding:
    """"""

    file: str
    value: str
    line: str

    evidence: Evidence

    full_value: str

    commit: str = "no value available"
    author: str = "no value available"
    email: str = "no value available"
    date: str = "no value available"

    def copy(self):
        return SecretFinding(
            evidence=self.evidence,
            file=self.file,
            value=self.value,
            full_value=self.full_value,
            line=self.line,
        )

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def json(self) -> dict:
        return {
            "File": self.file,
            "Value": self.value,
            "Line": self.line,
            "Full_Value": self.full_value,
            "Evidence": str(self.evidence),
            "Commit": self.commit,
            "Author": self.author,
            "Email": self.email,
            "Date": self.date,
        }


