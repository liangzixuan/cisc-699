from __future__ import annotations

import argparse
import json
from pathlib import Path

from safeexec.models import ExecutionRequest
from safeexec.service import execute_code


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Execute Python through SafeExec.")
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--code", help="Python source to execute")
    input_group.add_argument("--file", type=Path, help="Path to a Python source file")
    parser.add_argument("--backend", default="local")
    parser.add_argument("--wall-seconds", type=float, default=5.0)
    args = parser.parse_args(argv)

    code = args.code if args.code is not None else args.file.read_text(encoding="utf-8")
    request = ExecutionRequest.from_mapping(
        {
            "code": code,
            "backend": args.backend,
            "limits": {"wall_seconds": args.wall_seconds},
        }
    )
    result = execute_code(request)
    print(json.dumps(result.to_dict(), indent=2, sort_keys=True))
    return 0 if result.status == "ok" else 1
