from src.mapping.abc.parser import Parser
from src.dataclasses.secret_finding import SecretFinding
from src.dataclasses.evidence import Evidence

from src.utils.remove_prefixes import remove_prefixes


class DSParser(Parser):

    def process(self, report: dict) -> list[SecretFinding]:
        """"""

        processed_secrets = []

        for finding_file, secrets in report.items():
            for secret in secrets:
                full_value = secret["line"] if len(secret["line"]) < 500 else secret["string"]
                processed_secrets.append(
                    SecretFinding(
                        file=remove_prefixes(finding_file, self.prefixes_to_remove),
                        value=secret["string"],
                        full_value=full_value,
                        line=secret["line_number"],
                        evidence=Evidence.LOW,
                    )
                )

        return processed_secrets
