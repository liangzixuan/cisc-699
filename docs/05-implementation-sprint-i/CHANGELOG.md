# Changelog

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from git
> history and W5 grading feedback. AI-drafted, student-revised. Full audit
> trail: `docs/ai-use-log.md`.

## w5-baseline - 2026-06-09

Commit: `3475ccf`  
Tag: `w5-baseline`  
Branch: `main`  

### Added

- `src/safeexec/` package skeleton.
- Execution request/result dataclasses and limit metadata.
- Backend interface for local, Docker, and future gVisor execution.
- Development-only local subprocess backend.
- Docker/gVisor command builder with planned no-network, non-root, read-only,
  capability-drop, PID-limit, memory-limit, CPU-limit, and tmpfs controls.
- JSON API shell with `GET /health` and `POST /execute`.
- CLI entry point for manual execution.
- `make smoke`, `make test`, and `make api` targets.
- Functional tests for local execution, timeout handling, API response shape,
  Docker hardening command controls, and gVisor runtime selection.
- W5 Canvas check-in DOCX/PDF and local smoke/test/benchmark evidence.

### Known limitations

- The local backend is not a security sandbox.
- Docker/gVisor execution must still be verified on the Ubuntu droplet.
- Functional corpus and adversarial suite are seeds, not final evaluation sets.

## w5-evidence-addendum - 2026-06-17

### Added

- Evidence index mapping W5 rubric requirements to concrete files.
- Repository snapshot and git-log evidence.
- Enhanced known-issues/risk log with severity, likelihood, owner, dates, and
  target resolution.
- Architecture notes and changelog.
- Fresh 2026-06-17 smoke and test output captures.
- Revised evidence addendum DOCX/PDF for resubmission.
