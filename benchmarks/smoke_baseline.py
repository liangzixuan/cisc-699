from __future__ import annotations

import statistics
import time

from safeexec.models import ExecutionRequest
from safeexec.service import execute_code


def main() -> int:
    durations = []
    for _ in range(5):
        request = ExecutionRequest.from_mapping(
            {"backend": "local", "code": "print(21 * 2)", "limits": {"wall_seconds": 2.0}}
        )
        started = time.perf_counter()
        result = execute_code(request)
        durations.append((time.perf_counter() - started) * 1000)
        if result.status != "ok" or result.stdout != "42\n":
            raise SystemExit(f"unexpected result: {result}")

    print(f"runs=5 median_ms={statistics.median(durations):.3f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
