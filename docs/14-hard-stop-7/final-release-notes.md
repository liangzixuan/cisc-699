# SafeExec Final Release Notes

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from
> repository status and final evidence outputs. AI-drafted, student-revised.
> Full audit trail: `docs/ai-use-log.md`.

## Release

SafeExec final integrated submission package for CISC 699 Hard Stop 7.

## Included

- Source package under `src/safeexec/`
- Functional tests under `tests/functional/`
- Validation and benchmark scripts under `scripts/`
- Reproducibility docs under `docs/reproducibility/`
- Final evidence under `docs/14-hard-stop-7/evidence/`
- Final technical report and presentation deck
- AI-use log and engineering log

## Main Commands

```bash
make smoke
make test
PYTHONPATH=src python3 scripts/run_validation_workflow.py --output-dir docs/14-hard-stop-7/evidence --repeat 3
PYTHONPATH=src python3 scripts/audit_reproducibility.py --output-dir docs/14-hard-stop-7/evidence
make final-artifact
```

## Known Limitations

- Local subprocess backend is not a security boundary.
- Docker/gVisor evidence depends on the Ubuntu target host.
- Local macOS evidence covers local/API validation only.
- HumanEval/MBPP and adversarial suite expansion remain future work at the
  original stretch-target scale.
- API shell is intentionally minimal and not production hardened.

## Archive Guidance

Keep these together for future retrieval:

- `Final-Technical-Report.pdf`
- `Final-Presentation-and-Demo-Deck.pptx`
- `safeexec-final-artifact-package.zip`
- `final-evidence.zip`
- `docs/ai-use-log.md`
- repository commit hash for the final submission
