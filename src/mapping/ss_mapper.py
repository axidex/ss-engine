from src.mapping.abc.mapper import Mapper

from src.dataclasses.secret_finding import SecretFinding
from src.dataclasses.evidence import Evidence

from src.exceptions.empty_report import EmptyReportsException


def get_aggregated_findings(reports: list[list[SecretFinding]]) -> set[SecretFinding]:
    """Aggregating by value"""

    aggregated_findings = set(reports[0])

    for report in reports[1:]:
        aggregated_findings &= set(report)

    return aggregated_findings


def merge_reports(reports: list[list[SecretFinding]]) -> list[SecretFinding]:

    return [finding for report in reports for finding in report]


def change_evidence(merged_findings: list[SecretFinding], aggregated_findings: set[SecretFinding]) -> list[SecretFinding]:

    for finding in merged_findings:
        if finding in aggregated_findings:
            finding.evidence = Evidence.HIGH

    return merged_findings


class SSMapper(Mapper):

    def match(self, reports: list[list[SecretFinding]]) -> list[SecretFinding]:

        return change_evidence(
            merge_reports(reports),
            aggregated_findings=get_aggregated_findings(reports)
        )

    def map(self, reports: list[list[SecretFinding]]) -> list[SecretFinding]:
        """Mapping DS and GL reports {low: DS, medium: GL, high: Both}"""

        if not reports:
            raise EmptyReportsException("No reports provided")

        findings: list[SecretFinding] = self.match(reports)

        return findings
