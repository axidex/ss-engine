from src.mapping.abc.parser import Parser
from src.dataclasses.secret_finding import SecretFinding
from src.dataclasses.evidence import Evidence

from src.utils.remove_prefixes import remove_prefixes


class GLParser(Parser):

    def process(self, report: dict) -> list[SecretFinding]:
        """"""

        processed_secrets = []

        for secret in report:
            full_value = secret["Match"] if len(secret["Match"]) < 500 else secret["Secret"]
            processed_secrets.append(
                SecretFinding(
                    file=remove_prefixes(secret["File"], self.prefixes_to_remove),
                    value=secret["Secret"],
                    full_value=full_value,
                    line=secret["StartLine"],
                    evidence=Evidence.MEDIUM,
                )
            )

        return processed_secrets
