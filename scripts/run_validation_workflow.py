from __future__ import annotations

import argparse
import json
import threading
import time
from datetime import datetime, timezone
from http.server import HTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from safeexec.api.server import make_handler
from safeexec.models import ExecutionRequest
from safeexec.service import execute_code


LOCAL_CASES = [
    {
        "name": "hello_stdout",
        "code": "print('hello validation')",
        "expect_status": "ok",
        "expect_stdout": "hello validation\n",
    },
    {
        "name": "deterministic_arithmetic",
        "code": "print(sum(i * i for i in range(10)))",
        "expect_status": "ok",
        "expect_stdout": "285\n",
    },
    {
        "name": "stderr_and_exit_code",
        "code": "import sys\nprint('warn', file=sys.stderr)\nsys.exit(3)",
        "expect_status": "error",
        "expect_exit_code": 3,
        "expect_stderr": "warn\n",
    },
    {
        "name": "timeout_control",
        "code": "while True:\n    pass\n",
        "expect_status": "timeout",
        "limits": {"wall_seconds": 0.2},
    },
]

DOCKER_CASES = [
    {
        "name": "container_hello",
        "code": "import os, platform\nprint('uid=' + str(os.getuid()))\nprint('python=' + platform.python_version())",
        "expect_status": "ok",
    },
    {
        "name": "network_disabled_probe",
        "code": (
            "import socket\n"
            "sock = socket.socket()\n"
            "sock.settimeout(1)\n"
            "try:\n"
            "    sock.connect(('1.1.1.1', 53))\n"
            "    print('network-open')\n"
            "except Exception as exc:\n"
            "    print(type(exc).__name__)\n"
        ),
        "expect_status": "ok",
        "expect_not_stdout": "network-open\n",
        "limits": {"wall_seconds": 3.0},
    },
]


def run_case(backend: str, case: dict[str, object], iteration: int) -> dict[str, object]:
    limits = {"wall_seconds": 2.0, "output_limit_bytes": 20_000}
    limits.update(case.get("limits", {}))
    request = ExecutionRequest.from_mapping(
        {
            "backend": backend,
            "code": case["code"],
            "limits": limits,
        }
    )
    result = execute_code(request)
    result_dict = result.to_dict()
    passed = result.status == case.get("expect_status")
    if "expect_stdout" in case:
        passed = passed and result.stdout == case["expect_stdout"]
    if "expect_stderr" in case:
        passed = passed and result.stderr == case["expect_stderr"]
    if "expect_exit_code" in case:
        passed = passed and result.exit_code == case["expect_exit_code"]
    if "expect_not_stdout" in case:
        passed = passed and result.stdout != case["expect_not_stdout"]

    return {
        "backend": backend,
        "case": case["name"],
        "iteration": iteration,
        "passed": passed,
        "expectation": {
            key: value for key, value in case.items() if key.startswith("expect_")
        },
        "result": result_dict,
    }


def run_api_trace(output_dir: Path) -> dict[str, object]:
    server = HTTPServer(("127.0.0.1", 0), make_handler("local"))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    url = f"http://127.0.0.1:{server.server_port}/execute"
    request_body = {"code": "print('api validation')", "limits": {"wall_seconds": 2.0}}
    started = time.perf_counter()
    try:
        request = Request(
            url,
            data=json.dumps(request_body).encode("utf-8"),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request, timeout=5) as response:
            response_body = json.loads(response.read().decode("utf-8"))
            status_code = response.status
    except HTTPError as exc:
        response_body = {"error": exc.read().decode("utf-8")}
        status_code = exc.code
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)

    elapsed_ms = round((time.perf_counter() - started) * 1000, 3)
    trace = {
        "url": url,
        "status_code": status_code,
        "duration_ms": elapsed_ms,
        "request": request_body,
        "response": response_body,
        "passed": status_code == 200 and response_body.get("stdout") == "api validation\n",
    }
    (output_dir / "api-trace.json").write_text(json.dumps(trace, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return trace


def summarize(records: list[dict[str, object]], api_trace: dict[str, object]) -> dict[str, object]:
    by_backend: dict[str, dict[str, int]] = {}
    for record in records:
        bucket = by_backend.setdefault(record["backend"], {"passed": 0, "failed": 0, "total": 0})
        bucket["total"] += 1
        if record["passed"]:
            bucket["passed"] += 1
        else:
            bucket["failed"] += 1
    return {
        "total_records": len(records),
        "by_backend": by_backend,
        "api_trace_passed": api_trace["passed"],
        "all_passed": all(record["passed"] for record in records) and api_trace["passed"],
    }


def write_report(
    output_dir: Path,
    records: list[dict[str, object]],
    api_trace: dict[str, object],
    include_docker: bool,
) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    summary = summarize(records, api_trace)
    payload = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "include_docker": include_docker,
        "summary": summary,
        "api_trace": api_trace,
        "records": records,
    }
    (output_dir / "validation-results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    lines = [
        "SafeExec validation workflow",
        f"captured_at: {payload['captured_at']}",
        f"include_docker: {include_docker}",
        f"all_passed: {summary['all_passed']}",
        "",
        "Backend summary:",
    ]
    for backend, data in summary["by_backend"].items():
        lines.append(f"- {backend}: {data['passed']}/{data['total']} passed")
    lines.extend(
        [
            f"- api_trace: {'passed' if summary['api_trace_passed'] else 'failed'}",
            "",
            "Case details:",
        ]
    )
    for record in records:
        result = record["result"]
        lines.append(
            f"- {record['backend']}::{record['case']}#{record['iteration']} "
            f"{'PASS' if record['passed'] else 'FAIL'} "
            f"status={result['status']} exit={result['exit_code']} "
            f"reason={result['containment_reason']}"
        )
    (output_dir / "validation-summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(output_dir / "validation-results.json")
    print(output_dir / "validation-summary.txt")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run repeatable SafeExec validation workflow.")
    parser.add_argument("--output-dir", type=Path, default=Path("docs/06-hard-stop-3/evidence"))
    parser.add_argument("--repeat", type=int, default=3)
    parser.add_argument("--include-docker", action="store_true")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    records = []
    for iteration in range(1, args.repeat + 1):
        for case in LOCAL_CASES:
            records.append(run_case("local", case, iteration))
    if args.include_docker:
        for backend in ["docker", "gvisor"]:
            for iteration in range(1, args.repeat + 1):
                for case in DOCKER_CASES:
                    records.append(run_case(backend, case, iteration))
    api_trace = run_api_trace(args.output_dir)
    write_report(args.output_dir, records, api_trace, args.include_docker)
    return 0 if summarize(records, api_trace)["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
