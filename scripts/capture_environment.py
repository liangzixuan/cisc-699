from __future__ import annotations

import argparse
import json
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


def run_command(command: list[str], timeout: float = 10.0) -> dict[str, object]:
    try:
        completed = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
    except FileNotFoundError as exc:
        return {
            "command": command,
            "available": False,
            "returncode": None,
            "stdout": "",
            "stderr": str(exc),
        }
    except subprocess.TimeoutExpired as exc:
        return {
            "command": command,
            "available": True,
            "returncode": None,
            "stdout": exc.stdout or "",
            "stderr": exc.stderr or "timeout",
        }

    return {
        "command": command,
        "available": True,
        "returncode": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
    }


def build_snapshot() -> dict[str, object]:
    return {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "platform": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "platform": platform.platform(),
            "python": sys.version.replace("\n", " "),
            "python_executable": sys.executable,
        },
        "tools": {
            "git": run_command(["git", "--version"]),
            "docker_client": run_command(["docker", "version"]),
            "docker_info": run_command(["docker", "info"], timeout=15.0),
            "runsc": run_command(["runsc", "--version"]),
            "make": run_command(["make", "--version"]),
        },
        "repository": {
            "head": run_command(["git", "rev-parse", "HEAD"]),
            "branch": run_command(["git", "branch", "--show-current"]),
            "status": run_command(["git", "status", "--short", "--branch"]),
            "latest_commits": run_command(["git", "log", "--oneline", "--decorate", "--max-count=8"]),
            "docker_path": shutil.which("docker"),
            "runsc_path": shutil.which("runsc"),
        },
    }


def write_outputs(snapshot: dict[str, object], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "environment-snapshot.json"
    txt_path = output_dir / "environment-snapshot.txt"
    json_path.write_text(json.dumps(snapshot, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    platform_info = snapshot["platform"]
    tools = snapshot["tools"]
    repo = snapshot["repository"]
    lines = [
        "SafeExec environment snapshot",
        f"captured_at: {snapshot['captured_at']}",
        f"system: {platform_info['system']} {platform_info['release']} {platform_info['machine']}",
        f"python: {platform_info['python']}",
        f"git_head: {repo['head']['stdout']}",
        f"branch: {repo['branch']['stdout']}",
        "",
        "Tool status:",
    ]
    for name, result in tools.items():
        status = "ok" if result["returncode"] == 0 else "not-ready"
        first_line = (result["stdout"] or result["stderr"] or "").splitlines()
        summary = first_line[0] if first_line else ""
        lines.append(f"- {name}: {status} {summary}")
    txt_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json_path)
    print(txt_path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Capture SafeExec environment/toolchain evidence.")
    parser.add_argument("--output-dir", type=Path, default=Path("docs/06-hard-stop-3/evidence"))
    args = parser.parse_args()
    write_outputs(build_snapshot(), args.output_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
