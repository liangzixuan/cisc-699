from __future__ import annotations

from abc import ABC, abstractmethod

from safeexec.models import ExecutionRequest, ExecutionResult


class ExecutionBackend(ABC):
    """Interface shared by local, Docker, and future gVisor backends."""

    name: str

    @abstractmethod
    def execute(self, request: ExecutionRequest) -> ExecutionResult:
        """Run a Python execution request and return structured evidence."""
