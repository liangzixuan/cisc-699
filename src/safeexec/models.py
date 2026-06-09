from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class ExecutionLimits:
    wall_seconds: float = 5.0
    memory_mb: int = 128
    cpus: float = 1.0
    pids: int = 64
    output_limit_bytes: int = 20_000
    tmpfs_mb: int = 64

    @classmethod
    def from_mapping(cls, value: dict[str, Any] | None) -> "ExecutionLimits":
        if not value:
            return cls()
        allowed = {field.name for field in cls.__dataclass_fields__.values()}
        clean = {key: item for key, item in value.items() if key in allowed}
        return cls(**clean)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class ExecutionRequest:
    code: str
    backend: str = "local"
    limits: ExecutionLimits = ExecutionLimits()

    @classmethod
    def from_mapping(cls, value: dict[str, Any]) -> "ExecutionRequest":
        code = value.get("code")
        if not isinstance(code, str) or not code.strip():
            raise ValueError("request field 'code' must be a non-empty string")
        backend = value.get("backend", "local")
        if not isinstance(backend, str):
            raise ValueError("request field 'backend' must be a string")
        return cls(
            code=code,
            backend=backend,
            limits=ExecutionLimits.from_mapping(value.get("limits")),
        )


@dataclass(frozen=True)
class ExecutionResult:
    status: str
    backend: str
    exit_code: int | None
    stdout: str
    stderr: str
    duration_ms: float
    contained: bool
    containment_reason: str
    limits: ExecutionLimits

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["limits"] = self.limits.to_dict()
        return data
