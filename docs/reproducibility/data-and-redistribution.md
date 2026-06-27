# Data, Sources, and Redistribution Note

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app).
> AI-drafted, student-revised. Full audit trail: `docs/ai-use-log.md`.

SafeExec does not currently redistribute a third-party benchmark dataset inside
the repository. The committed validation cases are student-authored Python
snippets embedded in scripts and tests.

## Current included data

| Item | Location | Provenance | Redistribution status |
|---|---|---|---|
| Functional smoke cases | `tests/functional/`, `scripts/run_validation_workflow.py` | Student-authored project tests | Included in repo. |
| W8 midpoint cases | `scripts/run_midpoint_evidence.py` | Student-authored project tests | Included in repo. |
| Evidence outputs | `docs/06-hard-stop-3/`, `docs/08-hard-stop-4/`, `docs/10-hard-stop-5/` | Generated from local/target runs | Included as course evidence. |
| HumanEval/MBPP subsets | Not yet vendored | Planned public benchmark subsets | Must record task IDs, licenses, and any copied prompts before inclusion. |

## Future dataset rules

1. Prefer task-ID manifests over vendoring entire public datasets.
2. Preserve upstream license notices if any benchmark prompt or expected output
   is copied into the repository.
3. Do not include confidential, proprietary, FERPA, HIPAA, or personal data.
4. Record dataset version, retrieval date, and transformation steps in this
   document before final report submission.

