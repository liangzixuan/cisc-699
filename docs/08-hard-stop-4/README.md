# W8 Hard Stop 4: Midpoint Technical Evidence Review

This folder contains the Canvas submission package for **08 Hard Stop 4:
Midpoint Technical Evidence Review**.

## Primary files

| File | Purpose |
|---|---|
| `Midpoint-Technical-Evidence-Review.docx` | Canvas-ready editable package. |
| `Midpoint-Technical-Evidence-Review.pdf` | Canvas-ready PDF package. |
| `midpoint-technical-evidence-review.md` | Markdown source for the package. |
| `known-issues-risk-log.md` | W8 risk/issue log updated from benchmark evidence. |
| `canvas-submission-checklist.md` | Exact Canvas upload list and text-entry blurb. |

## Evidence folders

| Folder | Contents |
|---|---|
| `evidence-local/` | Local macOS environment snapshot, unit-test output, local-backend benchmark JSON/CSV/summary. |
| `evidence-target/` | Ubuntu target-host Docker/gVisor benchmark JSON/CSV/summary, environment snapshot, image/runtime metadata, script hash. |

## Reproduction commands

Local authoring-machine evidence:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests/functional -p 'test_*.py'
PYTHONPATH=src python3 scripts/capture_environment.py --output-dir docs/08-hard-stop-4/evidence-local
PYTHONPATH=src python3 scripts/run_midpoint_evidence.py --output-dir docs/08-hard-stop-4/evidence-local --repeat 5 --backends local
```

Target-host evidence:

```bash
PYTHONPATH=src python3 scripts/capture_environment.py --output-dir docs/08-hard-stop-4/evidence-target
PYTHONPATH=src python3 scripts/run_midpoint_evidence.py --output-dir docs/08-hard-stop-4/evidence-target --repeat 5 --backends local docker gvisor
```

The target-host run produced 130 records: local 30/30, Docker 50/50, and gVisor
49/50. The one gVisor failure was a timeout on `tmpfs_write_allowed` under the
current wall-time budget.

