from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from capture_environment import build_snapshot, write_outputs


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "docs" / "12-hard-stop-6" / "evidence"


def run_command(
    name: str,
    command: list[str],
    output_dir: Path,
    *,
    timeout: float = 120.0,
) -> dict[str, object]:
    env = os.environ.copy()
    env["PYTHONPATH"] = "src"
    started = datetime.now(timezone.utc)
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            env=env,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        returncode = completed.returncode
        stdout = completed.stdout
        stderr = completed.stderr
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        returncode = None
        stdout = exc.stdout or ""
        stderr = exc.stderr or "timeout"
        timed_out = True

    transcript = output_dir / f"{name}-output.txt"
    transcript.write_text(
        "$ " + " ".join(command) + "\n\n"
        + (stdout or "")
        + ("\n" if stdout and not stdout.endswith("\n") else "")
        + (stderr or ""),
        encoding="utf-8",
    )
    return {
        "name": name,
        "command": command,
        "started_at": started.isoformat(),
        "returncode": returncode,
        "timed_out": timed_out,
        "stdout_file": transcript.name,
        "passed": returncode == 0 and not timed_out,
    }


def copy_if_exists(source: Path, destination: Path) -> None:
    if source.exists():
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture W12 final SafeExec evidence.")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--repeat", type=int, default=3)
    args = parser.parse_args()

    output_dir = args.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    commands = [
        ("smoke", ["make", "smoke"], 60.0),
        ("unit-tests", ["make", "test"], 60.0),
        (
            "local-validation",
            [
                "python3",
                "scripts/run_validation_workflow.py",
                "--output-dir",
                str(output_dir),
                "--repeat",
                str(args.repeat),
            ],
            120.0,
        ),
        (
            "reproducibility-audit",
            ["python3", "scripts/audit_reproducibility.py", "--output-dir", str(output_dir)],
            60.0,
        ),
    ]
    records = [
        run_command(name, command, output_dir, timeout=timeout)
        for name, command, timeout in commands
    ]

    write_outputs(build_snapshot(), output_dir)
    copy_if_exists(ROOT / "docs/08-hard-stop-4/evidence-target/midpoint-summary.md", output_dir / "w8-target-midpoint-summary.md")
    copy_if_exists(ROOT / "docs/08-hard-stop-4/evidence-target/midpoint-summary.csv", output_dir / "w8-target-midpoint-summary.csv")
    copy_if_exists(ROOT / "docs/08-hard-stop-4/evidence-target/runsc-version.txt", output_dir / "w8-target-runsc-version.txt")
    copy_if_exists(ROOT / "docs/10-hard-stop-5/evidence/clean-run-output.txt", output_dir / "w10-clean-run-output.txt")

    summary = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "repeat": args.repeat,
        "all_passed": all(record["passed"] for record in records),
        "commands": records,
        "referenced_prior_evidence": [
            "w8-target-midpoint-summary.md",
            "w8-target-midpoint-summary.csv",
            "w8-target-runsc-version.txt",
            "w10-clean-run-output.txt",
        ],
    }
    (output_dir / "final-evidence-summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    lines = [
        "SafeExec final evidence summary",
        f"captured_at: {summary['captured_at']}",
        f"repeat: {args.repeat}",
        f"all_passed: {summary['all_passed']}",
        "",
        "Commands:",
    ]
    for record in records:
        lines.append(
            f"- {record['name']}: {'PASS' if record['passed'] else 'FAIL'} "
            f"returncode={record['returncode']} transcript={record['stdout_file']}"
        )
    lines.extend(
        [
            "",
            "Referenced prior target-host evidence:",
            "- w8-target-midpoint-summary.md",
            "- w8-target-midpoint-summary.csv",
            "- w8-target-runsc-version.txt",
            "- w10-clean-run-output.txt",
        ]
    )
    (output_dir / "final-evidence-summary.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(output_dir / "final-evidence-summary.txt")
    return 0 if summary["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
