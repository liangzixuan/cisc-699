# W12 Known-Issues and Final-Readiness Risk Log

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from
> W8-W12 evidence and prior risk logs. AI-drafted, student-revised. Full audit
> trail: `docs/ai-use-log.md`.

| ID | Issue / risk | Severity | Likelihood | Owner | Status | Evidence | Target resolution | Mitigation / next action |
|---|---|---:|---:|---|---|---|---|---|
| W12-R1 | Final HumanEval/MBPP subset manifest is not yet complete. | High | High | Zixuan Liang | Open | W3 requirements, W12 report draft | W13 | Add task IDs, provenance, license notes, expected-output policy, and final pass table. |
| W12-R2 | Full adversarial suite is not yet at approved count/category target. | High | High | Zixuan Liang | Open | `tests/adversarial/taxonomy.md` | W13 | Complete manifest-driven programs across approved categories and run on Docker/gVisor. |
| W12-R3 | gVisor timing needs cold-start versus warm-run separation. | Medium | High | Zixuan Liang | Open | W8 `tmpfs_write_allowed` timeout | W13 | Add benchmark mode or report fields that distinguish startup from program runtime. |
| W12-R4 | Docker/gVisor checks remain target-host evidence rather than local macOS evidence. | Medium | High | Zixuan Liang | Accepted limitation | W8 target-host evidence; W12 environment snapshot | W14 | Keep Ubuntu target host as official benchmark environment and document host facts. |
| W12-R5 | Final report/deck still require final result refresh after corpus expansion. | Medium | High | Zixuan Liang | Open | W12 draft package | W14 | Rebuild report/deck after final benchmark and update all tables consistently. |
| W12-R6 | AI-use appendix must remain complete through final revisions. | Medium | Medium | Zixuan Liang | Open | `docs/ai-use-log.md` | W14 | Continue logging each AI-assisted drafting, coding, and evidence-synthesis step. |
