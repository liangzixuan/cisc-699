# W8 Known-Issues and Risk Log

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from
> midpoint benchmark evidence and prior project logs. AI-drafted,
> student-revised. Full audit trail: `docs/ai-use-log.md`.

| ID | Issue / risk | Severity | Likelihood | Owner | Status | Evidence | Target resolution | Mitigation / next action |
|---|---|---:|---:|---|---|---|---|---|
| W8-R1 | gVisor shows higher tail latency than Docker and one `tmpfs_write_allowed` run timed out at the current wall-time boundary. | High | Medium | Zixuan Liang | Open | `evidence-target/midpoint-summary.md` | W9 | Separate container startup allowance from program wall-time budget; report cold-start and warm-run timing separately; rerun gVisor with >=30 samples. |
| W8-R2 | W8 case set is still a controlled 10-case batch, not the full HumanEval/MBPP subset or adversarial taxonomy. | High | High | Zixuan Liang | Open | `scripts/run_midpoint_evidence.py` | W9-W10 | Add corpus manifest with task IDs/provenance and expand from midpoint probes to functional/adversarial suites. |
| W8-R3 | Target host has Docker/gVisor but host Python remains 3.10.12 and `make` is unavailable. | Medium | High | Zixuan Liang | Open | `evidence-target/environment-snapshot.txt` | W9 | Install `make` and Python 3.11, or run the harness in a Python 3.11 dev container with documented commands. |
| W8-R4 | Local macOS machine cannot run Docker/gVisor, so container evidence depends on the Ubuntu validation host. | Medium | High | Zixuan Liang | Accepted limitation | `evidence-local/environment-snapshot.txt` | W14 | Treat the Ubuntu host as official benchmark environment; keep local machine for authoring and dev-only tests. |
| W8-R5 | Current timing captures end-to-end backend duration but does not yet distinguish image pull, cold start, warm start, Python startup, and program execution. | High | High | Zixuan Liang | Open | `evidence-target/midpoint-results.json` | W9 | Add warmup/pre-pull phase, explicit cold/warm labels, and per-condition summary fields. |
| W8-R6 | Benchmark script was copied into the target checkout before the final W8 package commit, so repeatability depends on the recorded script hash and repository package state. | Low | Medium | Zixuan Liang | Mitigated | `evidence-target/run-midpoint-evidence-sha256.txt` | W8 | Commit the W8 script and package; reference the final commit in Canvas text. |

