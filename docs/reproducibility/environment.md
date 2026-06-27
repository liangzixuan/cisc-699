# Environment and Configuration Notes

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app).
> AI-drafted, student-revised. Full audit trail: `docs/ai-use-log.md`.

## Runtime matrix

| Layer | Current requirement | Notes |
|---|---|---|
| Host Python | Python 3.11+ | Declared in `pyproject.toml`; current source uses only standard library modules. |
| Local backend | macOS or Linux with Python | Development smoke path only; not containment evidence. |
| Docker backend | Linux host with Docker and `python:3.11-slim` | Official container validation path. |
| gVisor backend | Docker plus registered `runsc` runtime | Stronger isolation path; W8 showed higher tail latency. |
| API shell | Python stdlib HTTP server | Started by `make api`; no FastAPI/Uvicorn dependency yet. |

## Configuration surface

SafeExec currently has no required secrets, API tokens, external services, or
private datasets. Optional local settings are documented in `.env.example`.

Important knobs:

- `SAFEEXEC_DEFAULT_BACKEND`: `local`, `docker`, or `gvisor`.
- `SAFEEXEC_API_HOST`: default `127.0.0.1`.
- `SAFEEXEC_API_PORT`: default `8080`.
- `SAFEEXEC_CONTAINER_IMAGE`: default `python:3.11-slim`.
- `SAFEEXEC_REPEAT`: repeat count for validation/benchmark scripts.

The current code does not automatically load `.env`; the file is a reviewer
template and configuration contract for the hardening phase.

## Dependency policy

The current prototype intentionally uses the Python standard library only. This
keeps the W10 reproduction path small and reduces dependency ambiguity. If later
sprints add packages, they should be added to `requirements.txt` and described
here with version pins or a lockfile.

