# SafeExec Artifact Manifest

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app).
> AI-drafted, student-revised. Full audit trail: `docs/ai-use-log.md`.

## Core source

| Path | Purpose |
|---|---|
| `src/safeexec/models.py` | Request, limits, and result data models. |
| `src/safeexec/service.py` | Backend selection and service entry point. |
| `src/safeexec/backends/local_subprocess.py` | Development-only local execution backend. |
| `src/safeexec/backends/docker.py` | Hardened Docker/gVisor command builder and executor. |
| `src/safeexec/api/server.py` | Minimal JSON `/execute` API shell. |
| `src/safeexec/cli.py` | CLI entry point. |

## Validation and evidence scripts

| Path | Purpose |
|---|---|
| `scripts/smoke_safeexec.py` | One-command local smoke test. |
| `scripts/capture_environment.py` | Environment/toolchain snapshot. |
| `scripts/run_validation_workflow.py` | W6 local/API/Docker/gVisor validation workflow. |
| `scripts/run_midpoint_evidence.py` | W8 benchmark/evidence workflow. |
| `scripts/audit_reproducibility.py` | W10 reproducibility-material audit. |
| `scripts/package_artifact.py` | Builds a tar.gz source package excluding `.git` and caches. |

## Tests

| Path | Purpose |
|---|---|
| `tests/functional/test_local_subprocess.py` | Local backend behavior. |
| `tests/functional/test_docker_command.py` | Docker/gVisor command hardening controls. |
| `tests/functional/test_api_server.py` | JSON API response behavior. |
| `tests/functional/test_validation_workflow.py` | Validation helper behavior. |

## Reproducibility documentation

| Path | Purpose |
|---|---|
| `README.md` | Primary project overview and setup entry point. |
| `.env.example` | Configuration template with no secrets. |
| `docs/reproducibility/runbook.md` | Fresh setup and validation commands. |
| `docs/reproducibility/environment.md` | Runtime, configuration, and dependency notes. |
| `docs/reproducibility/data-and-redistribution.md` | Data/source and redistribution policy. |
| `docs/ai-use-log.md` | AI-use audit trail. |
| `engineering-log.md` | Engineering process log. |

