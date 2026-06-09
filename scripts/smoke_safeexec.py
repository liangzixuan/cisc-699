from __future__ import annotations

import json

from safeexec.models import ExecutionRequest
from safeexec.service import execute_code


def main() -> int:
    request = ExecutionRequest.from_mapping(
        {
            "backend": "local",
            "code": "print('hello from safeexec sprint 1')",
            "limits": {"wall_seconds": 2.0, "output_limit_bytes": 2000},
        }
    )
    result = execute_code(request)
    print(json.dumps(result.to_dict(), indent=2, sort_keys=True))
    return 0 if result.status == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
