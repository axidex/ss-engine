from src.dataclasses.secret_finding import SecretFinding

from typing import Iterable


def validate_findings(findings: Iterable[SecretFinding]) -> list[SecretFinding]:
    """"""

    updated_findings = []

    for finding in findings:
        if len(finding.full_value) > 500:
            finding.full_value = finding.value

        updated_findings.append(finding)

    return updated_findings


def hide_findings(findings: Iterable[SecretFinding]) -> list[SecretFinding]:
    updated_findings = []

    for finding in findings:
        finding.value, finding.full_value = hide_full_secret(finding.value, finding.full_value)
        if len(finding.full_value) > 500:
            finding.full_value = finding.value

        updated_findings.append(finding)

    return updated_findings


def hide_secret(secret: str) -> str:
    return secret[:3] + "*" * 12


def hide_full_secret(secret: str, full_secret: str) -> tuple[str, str]:
    hide = hide_secret(secret)

    return hide, full_secret.replace(secret, hide)

