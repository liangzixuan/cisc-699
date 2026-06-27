# W10 Known-Issues and Reproducibility Risk Log

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from
> W10 reproducibility evidence and prior risk logs. AI-drafted,
> student-revised. Full audit trail: `docs/ai-use-log.md`.

| ID | Issue / risk | Severity | Likelihood | Owner | Status | Evidence | Target resolution | Mitigation / next action |
|---|---|---:|---:|---|---|---|---|---|
| W10-R1 | Docker/gVisor checks are not reproducible on the local macOS authoring machine. | Medium | High | Zixuan Liang | Accepted limitation | `docs/reproducibility/environment.md` | W14 | Continue using Ubuntu target host as official container benchmark environment. |
| W10-R2 | Target host previously lacked `make` and used host Python 3.10.12, while project target is Python 3.11+. | Medium | High | Zixuan Liang | Open | W8/W6 environment snapshots | W11 | Install Python 3.11 and `make`, or run validation harness inside a Python 3.11 dev container. |
| W10-R3 | Full HumanEval/MBPP and adversarial corpora are not yet packaged. | High | High | Zixuan Liang | Open | `docs/reproducibility/data-and-redistribution.md` | W11-W12 | Add task-ID manifest, license notes, expected-output policy, and provenance table. |
| W10-R4 | Reproducibility audit checks documentation completeness, but not semantic freshness of every generated evidence file. | Medium | Medium | Zixuan Liang | Open | `scripts/audit_reproducibility.py` | W12 | Extend audit to compare command outputs, package timestamp, and current commit. |
| W10-R5 | `.env.example` is a template; current code does not load `.env` automatically. | Low | Medium | Zixuan Liang | Documented | `.env.example`, `docs/reproducibility/environment.md` | W12 | Add config loader only if runtime configuration expands beyond current CLI/request fields. |

