from __future__ import annotations

import argparse
import tarfile
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "docs" / "10-hard-stop-5" / "safeexec-reproducibility-package.tar.gz"

EXCLUDE_PARTS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    "__pycache__",
    ".DS_Store",
}

EXCLUDE_SUFFIXES = {
    ".pyc",
    ".pyo",
    ".zip",
}


def should_include(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if any(part in EXCLUDE_PARTS for part in rel.parts):
        return False
    if path.suffix in EXCLUDE_SUFFIXES:
        return False
    if rel.parts[:2] == ("docs", "10-hard-stop-5") and path.name.endswith(".tar.gz"):
        return False
    return True


def build_package(output: Path) -> Path:
    output.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(output, "w:gz") as archive:
        for path in sorted(ROOT.rglob("*")):
            if not path.is_file() or not should_include(path):
                continue
            archive.add(path, arcname=Path("safeexec") / path.relative_to(ROOT))
        metadata = (
            "SafeExec reproducibility package\n"
            f"created_at: {datetime.now(timezone.utc).isoformat()}\n"
            "excludes: .git, caches, compiled Python files, generated package archives\n"
        ).encode("utf-8")
        info = tarfile.TarInfo("safeexec/PACKAGE-METADATA.txt")
        info.size = len(metadata)
        archive.addfile(info, fileobj=__import__("io").BytesIO(metadata))
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Build SafeExec reproducibility source package.")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    print(build_package(args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
