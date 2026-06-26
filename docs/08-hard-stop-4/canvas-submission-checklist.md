# Canvas Submission Checklist — W8 Midpoint Technical Evidence Review

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from the
> W8 package files and evidence folders. AI-drafted, student-revised. Full audit
> trail: `docs/ai-use-log.md`.

## Upload these files

Primary submission:

- `docs/08-hard-stop-4/Midpoint-Technical-Evidence-Review.pdf`
- `docs/08-hard-stop-4/Midpoint-Technical-Evidence-Review.docx`
- `docs/08-hard-stop-4/known-issues-risk-log.md`

Evidence:

- `docs/08-hard-stop-4/evidence-local/environment-snapshot.txt`
- `docs/08-hard-stop-4/evidence-local/local-test-output.txt`
- `docs/08-hard-stop-4/evidence-local/midpoint-summary.md`
- `docs/08-hard-stop-4/evidence-local/midpoint-results.csv`
- `docs/08-hard-stop-4/evidence-local/midpoint-results.json`
- `docs/08-hard-stop-4/evidence-target/environment-snapshot.txt`
- `docs/08-hard-stop-4/evidence-target/midpoint-summary.md`
- `docs/08-hard-stop-4/evidence-target/midpoint-results.csv`
- `docs/08-hard-stop-4/evidence-target/midpoint-results.json`
- `docs/08-hard-stop-4/evidence-target/docker-image-python311.txt`
- `docs/08-hard-stop-4/evidence-target/runsc-version.txt`
- `docs/08-hard-stop-4/evidence-target/run-midpoint-evidence-sha256.txt`
- `docs/ai-use-log.md`
- `engineering-log.md`

Optional convenience attachment:

- `docs/08-hard-stop-4/w8-evidence.zip`

## Suggested Canvas text-entry blurb

```text
Repository: https://github.com/liangzixuan/cisc-699

This Hard Stop 4 package focuses on one midpoint evidence question: whether the
current SafeExec execution path can repeatedly run correctness, failure-control,
and containment-oriented probes across local, hardened Docker, and gVisor
backends.

The target-host run generated 130 records: local 30/30 passed, Docker 50/50
passed, and gVisor 49/50 passed. The one failure was a gVisor
tmpfs_write_allowed timeout under the current wall-time budget, which is
documented as a timing-methodology risk rather than hidden. Supporting evidence
includes raw JSON/CSV outputs, environment snapshots, Docker/gVisor metadata,
script hash, risk log, AI-use log, and engineering log.
```

## Self-check before submitting

- [ ] Confirm the DOCX and PDF open correctly.
- [ ] Attach raw JSON/CSV evidence, not only screenshots or narrative.
- [ ] Include the risk log because it explains the gVisor timing weakness.
- [ ] Include the AI-use log and engineering log for academic-integrity/process evidence.
- [ ] Paste the repository URL and summary blurb into Canvas.
