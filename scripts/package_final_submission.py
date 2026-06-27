from __future__ import annotations

import argparse
import fnmatch
import json
import subprocess
import zipfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "docs" / "14-hard-stop-7" / "safeexec-final-artifact-package.zip"

INCLUDE_ROOTS = [
    "src",
    "tests",
    "benchmarks",
    "deploy",
    "scripts",
    "docs/reproducibility",
    "docs/08-hard-stop-4/evidence-target",
    "docs/10-hard-stop-5/evidence",
    "docs/12-hard-stop-6/evidence",
    "docs/14-hard-stop-7/evidence",
]
INCLUDE_FILES = [
    ".env.example",
    ".gitattributes",
    ".gitignore",
    "Makefile",
    "README.md",
    "pyproject.toml",
    "requirements.txt",
    "engineering-log.md",
    "docs/ai-use-log.md",
    "docs/14-hard-stop-7/final-integrated-submission.md",
    "docs/14-hard-stop-7/final-technical-report.md",
    "docs/14-hard-stop-7/final-test-evidence-appendix.md",
    "docs/14-hard-stop-7/final-release-notes.md",
    "docs/14-hard-stop-7/final-presentation-demo-script.md",
    "docs/14-hard-stop-7/canvas-submission-checklist.md",
    "docs/14-hard-stop-7/README.md",
]
EXCLUDE_PATTERNS = [
    "*/__pycache__/*",
    "*.pyc",
    "*.pyo",
    "*.DS_Store",
    "*/.DS_Store",
    "*.tmp",
    "*.bak",
    "*.tar",
    "*.tar.gz",
    "*.zip",
]


def should_exclude(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return any(fnmatch.fnmatch(rel, pattern) for pattern in EXCLUDE_PATTERNS)


def iter_files() -> list[Path]:
    files: set[Path] = set()
    for root in INCLUDE_ROOTS:
        base = ROOT / root
        if base.exists():
            files.update(path for path in base.rglob("*") if path.is_file())
    for item in INCLUDE_FILES:
        path = ROOT / item
        if path.exists() and path.is_file():
            files.add(path)
    return sorted(path for path in files if not should_exclude(path))


def run(command: list[str]) -> str:
    completed = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=False)
    output = (completed.stdout or completed.stderr or "").strip()
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Build the W14 final artifact ZIP.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    output = args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()

    manifest = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "git_head": run(["git", "rev-parse", "HEAD"]),
        "git_status": run(["git", "status", "--short", "--branch"]),
        "package_name": output.name,
        "included_files": [],
    }
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in iter_files():
            rel = path.relative_to(ROOT).as_posix()
            archive.write(path, rel)
            manifest["included_files"].append(rel)
        archive.writestr(
            "FINAL_PACKAGE_MANIFEST.json",
            json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        )

    manifest_path = output.with_suffix(".manifest.json")
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)
    print(manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
