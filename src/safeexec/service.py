from __future__ import annotations

from safeexec.backends import DockerBackend, LocalSubprocessBackend
from safeexec.models import ExecutionRequest, ExecutionResult


def execute_code(request: ExecutionRequest) -> ExecutionResult:
    return get_backend(request.backend).execute(request)


def get_backend(name: str):
    normalized = name.strip().lower()
    if normalized in {"local", "dev", "subprocess"}:
        return LocalSubprocessBackend()
    if normalized in {"docker", "hardened-docker", "hardened_docker"}:
        return DockerBackend()
    if normalized in {"gvisor", "runsc"}:
        return DockerBackend(runtime="runsc", name="gvisor")
    raise ValueError(f"unsupported backend: {name}")
