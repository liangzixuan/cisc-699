from __future__ import annotations

import subprocess
import time

from safeexec.backends.base import ExecutionBackend
from safeexec.models import ExecutionRequest, ExecutionResult


class DockerBackend(ExecutionBackend):
    """Docker/gVisor execution backend command builder.

    W5 commits the hardened command shape and API integration. Actual Docker and
    gVisor runs are expected on the Ubuntu target host recorded in the project
    engineering log.
    """

    def __init__(
        self,
        *,
        image: str = "python:3.11-slim",
        runtime: str | None = None,
        name: str = "hardened-docker",
    ) -> None:
        self.image = image
        self.runtime = runtime
        self.name = name

    def build_command(self, request: ExecutionRequest) -> list[str]:
        limits = request.limits
        command = [
            "docker",
            "run",
            "--rm",
            "--interactive",
            "--network",
            "none",
            "--cpus",
            str(limits.cpus),
            "--memory",
            f"{limits.memory_mb}m",
            "--pids-limit",
            str(limits.pids),
            "--read-only",
            "--cap-drop",
            "ALL",
            "--security-opt",
            "no-new-privileges",
            "--tmpfs",
            f"/tmp:rw,nosuid,nodev,size={limits.tmpfs_mb}m",
            "--workdir",
            "/tmp",
            "--user",
            "65534:65534",
        ]
        if self.runtime:
            command.extend(["--runtime", self.runtime])
        command.extend([self.image, "python", "-I", "-"])
        return command

    def execute(self, request: ExecutionRequest) -> ExecutionResult:
        limits = request.limits
        started = time.perf_counter()
        try:
            completed = subprocess.run(
                self.build_command(request),
                input=request.code.encode("utf-8"),
                capture_output=True,
                timeout=limits.wall_seconds + 1.0,
                check=False,
            )
        except FileNotFoundError as exc:
            return _backend_unavailable(self.name, str(exc), limits, started)
        except subprocess.TimeoutExpired as exc:
            duration_ms = (time.perf_counter() - started) * 1000
            return ExecutionResult(
                status="timeout",
                backend=self.name,
                exit_code=None,
                stdout=_decode(exc.stdout, limits.output_limit_bytes),
                stderr=_decode(exc.stderr, limits.output_limit_bytes),
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
            stdout=_decode(completed.stdout, limits.output_limit_bytes),
            stderr=_decode(completed.stderr, limits.output_limit_bytes),
            duration_ms=round(duration_ms, 3),
            contained=True,
            containment_reason="container_completed",
            limits=limits,
        )


def _backend_unavailable(
    backend: str,
    message: str,
    limits,
    started: float,
) -> ExecutionResult:
    duration_ms = (time.perf_counter() - started) * 1000
    return ExecutionResult(
        status="error",
        backend=backend,
        exit_code=None,
        stdout="",
        stderr=message,
        duration_ms=round(duration_ms, 3),
        contained=False,
        containment_reason="backend_unavailable",
        limits=limits,
    )


def _decode(value: bytes | str | None, limit: int) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        text = value
    else:
        text = value.decode("utf-8", errors="replace")
    if len(text.encode("utf-8")) <= limit:
        return text
    return text.encode("utf-8")[:limit].decode("utf-8", errors="ignore") + "\n...[truncated]"
