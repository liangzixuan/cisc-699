# W5 Known-Issues and Risk Log

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from W5
> grading feedback and the committed W5 evidence. AI-drafted, student-revised.
> Full audit trail: `docs/ai-use-log.md`.

| ID | Issue / risk | Severity | Likelihood | Owner | Status | Opened | Updated | Target resolution | Mitigation / next action |
|---|---|---:|---:|---|---|---|---|---|---|
| W5-R1 | Local subprocess backend is not a security sandbox. | High | Certain | Zixuan Liang | Accepted limitation | 2026-06-09 | 2026-06-17 | N/A | Label as dev-only everywhere; never use local results for containment claims. |
| W5-R2 | Docker/gVisor execution not yet verified in submitted W5 evidence. | High | Medium | Zixuan Liang | Open | 2026-06-09 | 2026-06-17 | W6 | Run Docker backend on Ubuntu droplet and capture command/API output. |
| W5-R3 | Functional corpus is still a seed, not the approved HumanEval/MBPP subset. | Medium | High | Zixuan Liang | Open | 2026-06-09 | 2026-06-17 | W6-W7 | Add corpus manifest with task IDs, provenance, and first >=30 functional programs. |
| W5-R4 | Adversarial suite contains taxonomy only. | High | High | Zixuan Liang | Open | 2026-06-09 | 2026-06-17 | W7 | Author program-level tests after Docker boundary is running, with expected contained outcomes. |
| W5-R5 | API shell uses Python stdlib HTTP server rather than FastAPI. | Low | Medium | Zixuan Liang | Accepted W5 tradeoff | 2026-06-09 | 2026-06-17 | Reassess W6 | Preserve response contract now; migrate only if FastAPI improves maintainability. |
| W5-R6 | Canvas upload omitted supporting evidence files, causing verification loss. | High | Resolved | Zixuan Liang | Resolved for resubmission package | 2026-06-17 | 2026-06-17 | 2026-06-17 | Add evidence index, repo link, commit/tag, setup files, logs, architecture notes, changelog, risk log, AI-use log, and engineering log. |

## Status Summary

The highest implementation risk remains W5-R2: the target Docker/gVisor backend
must be exercised on the Linux host before the project can make any containment
claim. The highest process risk from the W5 grade, W5-R6, is addressed by this
evidence addendum and attachment checklist.
