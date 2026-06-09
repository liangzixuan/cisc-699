from __future__ import annotations

import subprocess
import sys
import tempfile
import time
from pathlib import Path

from safeexec.backends.base import ExecutionBackend
from safeexec.models import ExecutionRequest, ExecutionResult


class LocalSubprocessBackend(ExecutionBackend):
    """Dev-only backend for reproducible W5 smoke tests.

    This backend is intentionally not a security boundary. It exists so the API,
    result schema, and functional-test harness can run on the authoring machine
    before Docker/gVisor execution is exercised on the Linux target host.
    """

    name = "local"

    def __init__(self, python_executable: str | None = None) -> None:
        self.python_executable = python_executable or sys.executable

    def execute(self, request: ExecutionRequest) -> ExecutionResult:
        limits = request.limits
        started = time.perf_counter()
        with tempfile.TemporaryDirectory(prefix="safeexec-") as workspace:
            script_path = Path(workspace) / "program.py"
            script_path.write_text(request.code, encoding="utf-8")
            try:
                completed = subprocess.run(
                    [self.python_executable, "-I", str(script_path)],
                    cwd=workspace,
                    env={
                        "PYTHONUNBUFFERED": "1",
                        "PYTHONDONTWRITEBYTECODE": "1",
                    },
                    capture_output=True,
                    timeout=limits.wall_seconds,
                    check=False,
                )
            except subprocess.TimeoutExpired as exc:
                duration_ms = (time.perf_counter() - started) * 1000
                return ExecutionResult(
                    status="timeout",
                    backend=self.name,
                    exit_code=None,
                    stdout=_decode_and_truncate(exc.stdout, limits.output_limit_bytes),
                    stderr=_decode_and_truncate(exc.stderr, limits.output_limit_bytes),
                    duration_ms=round(duration_ms, 3),
                    contained=True,
                    containment_reason="wall_timeout",
                    limits=limits,
                )

        duration_ms = (time.perf_counter() - started) * 1000
        status = "ok" if completed.returncode == 0 else "error"
        return ExecutionResult(
            status=status,
            backend=self.name,
            exit_code=completed.returncode,
            stdout=_decode_and_truncate(completed.stdout, limits.output_limit_bytes),
            stderr=_decode_and_truncate(completed.stderr, limits.output_limit_bytes),
            duration_ms=round(duration_ms, 3),
            contained=True,
            containment_reason="dev_subprocess_completed",
            limits=limits,
        )


def _decode_and_truncate(value: bytes | str | None, limit: int) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        text = value
    else:
        text = value.decode("utf-8", errors="replace")
    if len(text.encode("utf-8")) <= limit:
        return text
    encoded = text.encode("utf-8")[:limit]
    return encoded.decode("utf-8", errors="ignore") + "\n...[truncated]"
