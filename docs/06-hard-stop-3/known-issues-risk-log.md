# W6 Known-Issues and Risk Log

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from
> W6 validation output and project requirements. AI-drafted, student-revised.
> Full audit trail: `docs/ai-use-log.md`.

| ID | Issue / risk | Severity | Likelihood | Owner | Status | Evidence | Target resolution | Mitigation / next action |
|---|---|---:|---:|---|---|---|---|---|
| W6-R1 | First Docker validation run timed out while pulling `python:3.11-slim`. | Medium | Medium | Zixuan Liang | Mitigated | `evidence-target/validation-summary.txt` | W7 | Pre-pull and record image digest before timed validation; keep first-run log as reproducibility caveat. |
| W6-R2 | Target host lacks `make`, so Makefile targets could not run directly on the droplet. | Low | High | Zixuan Liang | Open | `evidence-target/environment-snapshot.txt` | W7 | Install `make` or document direct Python command equivalents in README. |
| W6-R3 | Droplet host Python is 3.10.12, below the declared Python >=3.11 project target. | Medium | High | Zixuan Liang | Open | `evidence-target/environment-snapshot.txt` | W7 | Use container Python 3.11 for backend execution; install host Python 3.11 or run harness inside a Python 3.11 dev container. |
| W6-R4 | Validation cases are smoke/integration checks, not the full HumanEval/MBPP functional corpus. | High | High | Zixuan Liang | Open | `evidence-target-rerun/validation-summary.txt` | W7-W8 | Add functional corpus manifest and expand to >=30, then >=100 tasks. |
| W6-R5 | Network-disabled probe verifies blocked outbound connection but does not yet classify richer adversarial categories. | High | High | Zixuan Liang | Open | `tests/adversarial/taxonomy.md` | W7-W8 | Add program-level adversarial tests by taxonomy after Docker/gVisor evidence path remains stable. |
| W6-R6 | Local macOS Docker daemon is unavailable, so container evidence depends on the Ubuntu droplet. | Medium | High | Zixuan Liang | Accepted limitation | `evidence/local-docker-version.txt` | W7 | Treat droplet as official validation environment; keep local machine for authoring and local/API tests. |
