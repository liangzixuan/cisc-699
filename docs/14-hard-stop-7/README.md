# Hard Stop 7: Final Integrated Submission and Presentation/Demo

This folder contains the final integrated SafeExec package for CISC 699.

## Primary Files

| File | Purpose |
|---|---|
| `Final-Technical-Report.docx` | Final report editable document |
| `Final-Technical-Report.pdf` | Final report PDF |
| `Final-Presentation-and-Demo-Deck.pptx` | Final presentation/demo deck |
| `Final-Presentation-and-Demo-Deck.pdf` | PDF export of the deck |
| `final-integrated-submission.md` | Canvas-facing package summary |
| `final-technical-report.md` | Markdown source for final report |
| `final-test-evidence-appendix.md` | Evidence appendix |
| `final-release-notes.md` | Release/archive notes |
| `final-presentation-demo-script.md` | Walkthrough/demo recording script |
| `canvas-submission-checklist.md` | Canvas upload checklist |
| `safeexec-final-artifact-package.zip` | Final computational artifact package |
| `final-evidence.zip` | Final evidence bundle |
| `evidence/` | Fresh final evidence and copied target-host evidence |

## Final Evidence Command

```bash
PYTHONPATH=src python3 scripts/run_final_evidence.py --output-dir docs/14-hard-stop-7/evidence --repeat 3
```

## Artifact Package Command

```bash
make final-artifact
```
