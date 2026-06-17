# W5 Architecture Notes

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from the
> committed W5 source tree and the approved W4 design package. AI-drafted,
> student-revised. Full audit trail: `docs/ai-use-log.md`.

## Purpose

The W5 architecture establishes a runnable spine for SafeExec without claiming
that the local development backend is a security sandbox. The design goal is to
stabilize the request/result contract and test harness before adding full
Docker and gVisor runtime evidence in W6-W8.

## Component Map

| Component | Path | Responsibility |
|---|---|---|
| Execution request/result models | `src/safeexec/models.py` | Defines structured inputs, limits, and output evidence fields. |
| Backend interface | `src/safeexec/backends/base.py` | Provides a common `execute()` contract for local, Docker, and future gVisor execution. |
| Local subprocess backend | `src/safeexec/backends/local_subprocess.py` | Development-only smoke path with timeout and output capture. Not a containment boundary. |
| Docker/gVisor command builder | `src/safeexec/backends/docker.py` | Encodes the planned isolation controls for target-host execution. |
| Service layer | `src/safeexec/service.py` | Selects the configured backend and runs an execution request. |
| HTTP API shell | `src/safeexec/api/server.py` | Provides `GET /health` and `POST /execute` using the current response contract. |
| CLI | `src/safeexec/cli.py` | Allows manual execution from the terminal for smoke checks. |
| Smoke script | `scripts/smoke_safeexec.py` | Runs one known-good local execution and prints JSON evidence. |
| Tests | `tests/functional/` | Verifies local execution, timeout behavior, API response shape, and Docker/gVisor command controls. |

## Backend Boundary

The `local` backend is intentionally labeled as a development backend. It runs a
Python subprocess on the authoring machine and supports only early functional
verification. It must not be used to claim adversarial containment.

The Docker/gVisor path is represented in W5 by command construction and tests
for the planned controls:

- no outbound network: `--network none`
- non-root process: `--user 65534:65534`
- read-only root filesystem: `--read-only`
- no Linux capabilities: `--cap-drop ALL`
- privilege escalation prevention: `--security-opt no-new-privileges`
- process limit: `--pids-limit`
- memory limit: `--memory`
- CPU limit: `--cpus`
- ephemeral workspace: `--tmpfs /tmp:rw,nosuid,nodev,size=...`
- gVisor runtime selector: `--runtime runsc`

## W6 Transition

The next implementation step is to run the Docker backend on the Ubuntu droplet
already recorded in the engineering log, capture the first real containerized
`POST /execute` output, and then convert the command controls into a documented
hardening profile.
