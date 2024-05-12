import json
import logging

from typing import Callable

from prometheus_fastapi_instrumentator.metrics import Info
from prometheus_client import Counter

logger = logging.getLogger(__name__)


def http_requested_practices() -> Callable[[Info], None]:
    metric_pract = Counter(
        "http_requested_practices",
        "Number of times a certain practices has been requested",
        labelnames=("practices",),
    )

    def instrumentation(info: Info) -> None:

        try:
            pract_arr = json.loads(info.response.body.decode("utf-8"))["applicable_practices"]

            for pract in pract_arr:
                metric_pract.labels(pract).inc()

        except Exception:
            pass

    return instrumentation


def http_codes() -> Callable[[Info], None]:
    metric_code = Counter(
        "http_codes",
        "Number of codes that api returned",
        labelnames=("codes",),
    )

    def instrumentation(info: Info) -> None:
        code = info.response.status_code
        metric_code.labels(code).inc()

    return instrumentation
