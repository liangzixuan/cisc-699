from __future__ import annotations

import argparse
import csv
import json
import statistics
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from safeexec.models import ExecutionRequest, ExecutionResult
from safeexec.service import execute_code


@dataclass(frozen=True)
class EvidenceCase:
    name: str
    category: str
    code: str
    expected_status: str
    backends: tuple[str, ...]
    limits: dict[str, Any]
    expected_stdout: str | None = None
    expected_stderr: str | None = None
    expected_exit_code: int | None = None
    stdout_contains: str | None = None
    stderr_contains: str | None = None
    stdout_not_contains: str | None = None


ALL_BACKENDS = ("local", "docker", "gvisor")

CASES = [
    EvidenceCase(
        name="functional_hello",
        category="correctness",
        code="print('midpoint evidence')",
        expected_status="ok",
        expected_stdout="midpoint evidence\n",
        backends=ALL_BACKENDS,
        limits={"wall_seconds": 2.0},
    ),
    EvidenceCase(
        name="deterministic_arithmetic",
        category="correctness",
        code="print(sum((i * i) % 17 for i in range(2000)))",
        expected_status="ok",
        expected_stdout="16008\n",
        backends=ALL_BACKENDS,
        limits={"wall_seconds": 2.0},
    ),
    EvidenceCase(
        name="json_serialization",
        category="correctness",
        code=(
            "import json\n"
            "payload = {'status': 'ok', 'values': [i * 3 for i in range(4)]}\n"
            "print(json.dumps(payload, sort_keys=True))"
        ),
        expected_status="ok",
        expected_stdout='{"status": "ok", "values": [0, 3, 6, 9]}\n',
        backends=ALL_BACKENDS,
        limits={"wall_seconds": 2.0},
    ),
    EvidenceCase(
        name="stderr_exit_code",
        category="correctness",
        code="import sys\nprint('controlled failure', file=sys.stderr)\nsys.exit(7)",
        expected_status="error",
        expected_stderr="controlled failure\n",
        expected_exit_code=7,
        backends=ALL_BACKENDS,
        limits={"wall_seconds": 2.0},
    ),
    EvidenceCase(
        name="wall_timeout",
        category="failure-control",
        code="while True:\n    pass\n",
        expected_status="timeout",
        backends=ALL_BACKENDS,
        limits={"wall_seconds": 0.4},
    ),
    EvidenceCase(
        name="output_truncation",
        category="failure-control",
        code="print('x' * 50000)",
        expected_status="ok",
        stdout_contains="...[truncated]",
        backends=ALL_BACKENDS,
        limits={"wall_seconds": 2.0, "output_limit_bytes": 2048},
    ),
    EvidenceCase(
        name="container_nonroot_uid",
        category="containment",
        code="import os\nprint(os.getuid())",
        expected_status="ok",
        expected_stdout="65534\n",
        backends=("docker", "gvisor"),
        limits={"wall_seconds": 2.0},
    ),
    EvidenceCase(
        name="container_readonly_root",
        category="containment",
        code=(
            "try:\n"
            "    open('/safeexec-write-probe', 'w').write('blocked')\n"
            "    print('root-write-open')\n"
            "except Exception as exc:\n"
            "    print(type(exc).__name__)\n"
        ),
        expected_status="ok",
        stdout_not_contains="root-write-open",
        backends=("docker", "gvisor"),
        limits={"wall_seconds": 2.0},
    ),
    EvidenceCase(
        name="tmpfs_write_allowed",
        category="containment",
        code=(
            "from pathlib import Path\n"
            "p = Path('/tmp/safeexec_tmp_probe.txt')\n"
            "p.write_text('ok', encoding='utf-8')\n"
            "print(p.read_text(encoding='utf-8'))"
        ),
        expected_status="ok",
        expected_stdout="ok\n",
        backends=("docker", "gvisor"),
        limits={"wall_seconds": 2.0},
    ),
    EvidenceCase(
        name="network_disabled_probe",
        category="containment",
        code=(
            "import socket\n"
            "sock = socket.socket()\n"
            "sock.settimeout(0.8)\n"
            "try:\n"
            "    sock.connect(('1.1.1.1', 53))\n"
            "    print('network-open')\n"
            "except Exception as exc:\n"
            "    print(type(exc).__name__)\n"
        ),
        expected_status="ok",
        stdout_not_contains="network-open",
        backends=("docker", "gvisor"),
        limits={"wall_seconds": 2.5},
    ),
]


def evaluate(case: EvidenceCase, result: ExecutionResult) -> tuple[bool, list[str]]:
    failures: list[str] = []
    if result.status != case.expected_status:
        failures.append(f"status expected {case.expected_status!r}, got {result.status!r}")
    if case.expected_stdout is not None and result.stdout != case.expected_stdout:
        failures.append(f"stdout expected {case.expected_stdout!r}, got {result.stdout!r}")
    if case.expected_stderr is not None and result.stderr != case.expected_stderr:
        failures.append(f"stderr expected {case.expected_stderr!r}, got {result.stderr!r}")
    if case.expected_exit_code is not None and result.exit_code != case.expected_exit_code:
        failures.append(f"exit expected {case.expected_exit_code!r}, got {result.exit_code!r}")
    if case.stdout_contains is not None and case.stdout_contains not in result.stdout:
        failures.append(f"stdout missing {case.stdout_contains!r}")
    if case.stderr_contains is not None and case.stderr_contains not in result.stderr:
        failures.append(f"stderr missing {case.stderr_contains!r}")
    if case.stdout_not_contains is not None and case.stdout_not_contains in result.stdout:
        failures.append(f"stdout unexpectedly contained {case.stdout_not_contains!r}")
    return not failures, failures


def run_case(case: EvidenceCase, backend: str, iteration: int) -> dict[str, Any]:
    request = ExecutionRequest.from_mapping(
        {"backend": backend, "code": case.code, "limits": case.limits}
    )
    started = time.perf_counter()
    result = execute_code(request)
    harness_ms = round((time.perf_counter() - started) * 1000, 3)
    passed, failures = evaluate(case, result)
    return {
        "backend": backend,
        "case": case.name,
        "category": case.category,
        "iteration": iteration,
        "passed": passed,
        "failures": failures,
        "harness_duration_ms": harness_ms,
        "result": result.to_dict(),
    }


def percentile(values: list[float], rank: float) -> float:
    if not values:
        return 0.0
    if len(values) == 1:
        return values[0]
    ordered = sorted(values)
    index = (len(ordered) - 1) * rank
    lower = int(index)
    upper = min(lower + 1, len(ordered) - 1)
    weight = index - lower
    return ordered[lower] * (1 - weight) + ordered[upper] * weight


def summarize(records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    groups: dict[tuple[str, str, str], list[dict[str, Any]]] = {}
    for record in records:
        key = (record["backend"], record["category"], record["case"])
        groups.setdefault(key, []).append(record)

    rows = []
    for (backend, category, case_name), group in sorted(groups.items()):
        durations = [float(record["result"]["duration_ms"]) for record in group]
        passed = sum(1 for record in group if record["passed"])
        rows.append(
            {
                "backend": backend,
                "category": category,
                "case": case_name,
                "passed": passed,
                "total": len(group),
                "pass_rate": round(passed / len(group), 4),
                "mean_ms": round(statistics.fmean(durations), 3),
                "median_ms": round(statistics.median(durations), 3),
                "p95_ms": round(percentile(durations, 0.95), 3),
                "min_ms": round(min(durations), 3),
                "max_ms": round(max(durations), 3),
            }
        )
    return rows


def write_outputs(output_dir: Path, records: list[dict[str, Any]], repeat: int, backends: list[str]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    summary_rows = summarize(records)
    payload = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "repeat": repeat,
        "requested_backends": backends,
        "case_count": len({record["case"] for record in records}),
        "record_count": len(records),
        "all_passed": all(record["passed"] for record in records),
        "summary": summary_rows,
        "records": records,
    }
    (output_dir / "midpoint-results.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    with (output_dir / "midpoint-results.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "backend",
                "case",
                "category",
                "iteration",
                "passed",
                "status",
                "exit_code",
                "duration_ms",
                "contained",
                "containment_reason",
            ],
        )
        writer.writeheader()
        for record in records:
            result = record["result"]
            writer.writerow(
                {
                    "backend": record["backend"],
                    "case": record["case"],
                    "category": record["category"],
                    "iteration": record["iteration"],
                    "passed": record["passed"],
                    "status": result["status"],
                    "exit_code": result["exit_code"],
                    "duration_ms": result["duration_ms"],
                    "contained": result["contained"],
                    "containment_reason": result["containment_reason"],
                }
            )

    with (output_dir / "midpoint-summary.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(summary_rows[0].keys()))
        writer.writeheader()
        writer.writerows(summary_rows)

    lines = [
        "SafeExec midpoint technical evidence",
        f"captured_at: {payload['captured_at']}",
        f"repeat: {repeat}",
        f"requested_backends: {', '.join(backends)}",
        f"record_count: {payload['record_count']}",
        f"all_passed: {payload['all_passed']}",
        "",
        "| Backend | Category | Case | Pass | Mean ms | Median ms | P95 ms | Range ms |",
        "|---|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in summary_rows:
        lines.append(
            f"| {row['backend']} | {row['category']} | {row['case']} | "
            f"{row['passed']}/{row['total']} | {row['mean_ms']:.3f} | "
            f"{row['median_ms']:.3f} | {row['p95_ms']:.3f} | "
            f"{row['min_ms']:.3f}-{row['max_ms']:.3f} |"
        )
    failures = [record for record in records if not record["passed"]]
    if failures:
        lines.extend(["", "Failures:"])
        for record in failures:
            lines.append(
                f"- {record['backend']}::{record['case']}#{record['iteration']}: "
                + "; ".join(record["failures"])
            )
    (output_dir / "midpoint-summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    (output_dir / "midpoint-summary.txt").write_text(
        "\n".join(line.replace("|", " ") for line in lines) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run midpoint evidence cases for SafeExec.")
    parser.add_argument("--output-dir", type=Path, default=Path("docs/08-hard-stop-4/evidence-local"))
    parser.add_argument("--repeat", type=int, default=5)
    parser.add_argument(
        "--backends",
        nargs="+",
        default=["local"],
        choices=list(ALL_BACKENDS),
        help="Backends to run. Container-only cases are skipped for local-only runs.",
    )
    args = parser.parse_args()

    records: list[dict[str, Any]] = []
    for iteration in range(1, args.repeat + 1):
        for case in CASES:
            for backend in args.backends:
                if backend not in case.backends:
                    continue
                records.append(run_case(case, backend, iteration))
    write_outputs(args.output_dir, records, args.repeat, args.backends)
    return 0 if all(record["passed"] for record in records) else 1


if __name__ == "__main__":
    raise SystemExit(main())
