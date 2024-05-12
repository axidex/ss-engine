from src.mapping.abc.servicer import Servicer

from src.dataclasses.secret_finding import SecretFinding
from src.dataclasses.evidence import Evidence

from src.mapping.ss_mapper import SSMapper
from src.mapping.ds_parser import DSParser
from src.mapping.gl_parser import GLParser

from typing import Iterable

from collections import OrderedDict

from src.utils.hide_findings import hide_findings


class SSServicer(Servicer):

    def __init__(self, prefixes_to_remove: list[str]):
        self.mapper = SSMapper()
        self.parsers = {
            "deepsecrets": DSParser(prefixes_to_remove),
            "gitleaks": GLParser(prefixes_to_remove)
        }

    def divide_reports(self, raw_reports: Iterable[dict]) -> list[list[SecretFinding]]:
        return [
            self.parsers[raw_reports["practiceTool"]].process(
                report=raw_report["scanResult"]
            )
            for raw_report in raw_reports
        ]

    def start(self, raw_reports: Iterable[dict]) -> dict[str, list[dict]]:
        """"""

        findings = self.mapper.map(reports=self.divide_reports(raw_reports=raw_reports))

        findings = hide_findings(findings)

        merged_dict = OrderedDict()

        merged_dict.update(
            {
                "LOW": [
                    finding.json()
                    for finding in findings
                    if finding.evidence == Evidence.LOW
                ]
            }
        )
        merged_dict.update(
            {
                "MEDIUM": [
                    finding.json()
                    for finding in findings
                    if finding.evidence == Evidence.MEDIUM
                ]
            }
        )
        merged_dict.update(
            {
                "HIGH": [
                    finding.json()
                    for finding in findings
                    if finding.evidence == Evidence.HIGH
                ]
            }
        )

        return merged_dict
