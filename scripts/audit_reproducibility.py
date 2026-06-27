from __future__ import annotations

import argparse
import json
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = [
    "README.md",
    "Makefile",
    "pyproject.toml",
    "requirements.txt",
    ".env.example",
    "src/safeexec",
    "tests/functional",
    "scripts/capture_environment.py",
    "scripts/run_validation_workflow.py",
    "scripts/run_midpoint_evidence.py",
    "scripts/package_artifact.py",
    "docs/reproducibility/runbook.md",
    "docs/reproducibility/environment.md",
    "docs/reproducibility/data-and-redistribution.md",
    "docs/reproducibility/artifact-manifest.md",
    "docs/ai-use-log.md",
    "engineering-log.md",
]

README_KEYWORDS = [
    "Setup, run, test",
    "make smoke",
    "make test",
    "make validate",
    "make midpoint",
    "AI-use disclosure",
]

MAKE_TARGETS = [
    "smoke",
    "test",
    "api",
    "env",
    "validate",
    "midpoint",
    "repro-audit",
    "package-artifact",
]


def run(command: list[str]) -> dict[str, object]:
    try:
        completed = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            timeout=20,
            check=False,
        )
    except Exception as exc:  # pragma: no cover - defensive evidence path
        return {"command": command, "ok": False, "error": str(exc)}
    return {
        "command": command,
        "ok": completed.returncode == 0,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def audit() -> dict[str, object]:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).exists()]
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    missing_readme_keywords = [item for item in README_KEYWORDS if item not in readme]
    makefile = (ROOT / "Makefile").read_text(encoding="utf-8")
    missing_make_targets = [
        target for target in MAKE_TARGETS if f"{target}:" not in makefile
    ]
    pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8")
    requirements = (ROOT / "requirements.txt").read_text(encoding="utf-8")
    commands = {
        "git_head": run(["git", "rev-parse", "HEAD"]),
        "git_status": run(["git", "status", "--short"]),
        "python_version": {
            "ok": True,
            "stdout": sys.version,
            "platform": platform.platform(),
        },
        "docker_version": run(["docker", "--version"]) if shutil.which("docker") else {"ok": False, "error": "docker not found"},
        "runsc_version": run(["runsc", "--version"]) if shutil.which("runsc") else {"ok": False, "error": "runsc not found"},
    }
    findings = []
    if missing:
        findings.append("required_paths_missing")
    if missing_readme_keywords:
        findings.append("readme_keywords_missing")
    if missing_make_targets:
        findings.append("make_targets_missing")
    if "requires-python = \">=3.11\"" not in pyproject:
        findings.append("python_requirement_not_declared")
    if "standard library" not in requirements.lower():
        findings.append("dependency_policy_unclear")

    return {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "root": str(ROOT),
        "all_required_paths_present": not missing,
        "missing_required_paths": missing,
        "readme_keywords_present": not missing_readme_keywords,
        "missing_readme_keywords": missing_readme_keywords,
        "make_targets_present": not missing_make_targets,
        "missing_make_targets": missing_make_targets,
        "pyproject_requires_python": ">=3.11" in pyproject,
        "dependency_policy": "standard library only" if "standard library" in requirements.lower() else "review",
        "commands": commands,
        "findings": findings,
        "passed": not findings,
    }


def write_outputs(output_dir: Path, payload: dict[str, object]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "reproducibility-audit.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    lines = [
        "# SafeExec Reproducibility Audit",
        "",
        f"- captured_at: {payload['captured_at']}",
        f"- passed: {payload['passed']}",
        f"- all_required_paths_present: {payload['all_required_paths_present']}",
        f"- readme_keywords_present: {payload['readme_keywords_present']}",
        f"- make_targets_present: {payload['make_targets_present']}",
        f"- dependency_policy: {payload['dependency_policy']}",
        "",
        "## Findings",
        "",
    ]
    findings = payload["findings"]
    if findings:
        lines.extend(f"- {item}" for item in findings)
    else:
        lines.append("- No blocking reproducibility findings from this audit.")
    lines.extend(["", "## Tool status", ""])
    commands = payload["commands"]
    for name, result in commands.items():
        if isinstance(result, dict):
            status = "ok" if result.get("ok") else "not-ready"
            first_line = str(result.get("stdout") or result.get("error") or "").splitlines()[0:1]
            suffix = f" - {first_line[0]}" if first_line else ""
            lines.append(f"- {name}: {status}{suffix}")
    (output_dir / "reproducibility-audit.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit SafeExec reproducibility materials.")
    parser.add_argument("--output-dir", type=Path, default=Path("docs/10-hard-stop-5/evidence"))
    args = parser.parse_args()
    payload = audit()
    write_outputs(args.output_dir, payload)
    print(args.output_dir / "reproducibility-audit.json")
    print(args.output_dir / "reproducibility-audit.md")
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
