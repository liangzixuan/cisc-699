# Canvas Submission Checklist — W10 Artifact Hardening and Reproducibility

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from the
> W10 package files and evidence folders. AI-drafted, student-revised. Full
> audit trail: `docs/ai-use-log.md`.

## Upload these files

Primary package:

- `docs/10-hard-stop-5/Artifact-Hardening-and-Reproducibility-Check.pdf`
- `docs/10-hard-stop-5/Artifact-Hardening-and-Reproducibility-Check.docx`
- `docs/10-hard-stop-5/safeexec-reproducibility-package.tar.gz`
- `docs/10-hard-stop-5/walkthrough-script.md`

Evidence:

- `docs/10-hard-stop-5/evidence/clean-run-output.txt`
- `docs/10-hard-stop-5/evidence/smoke-output.txt`
- `docs/10-hard-stop-5/evidence/test-output.txt`
- `docs/10-hard-stop-5/evidence/validation-summary.txt`
- `docs/10-hard-stop-5/evidence/reproducibility-audit.md`
- `docs/10-hard-stop-5/evidence/environment-snapshot.txt`
- `docs/reproducibility/runbook.md`
- `docs/reproducibility/environment.md`
- `docs/reproducibility/data-and-redistribution.md`
- `docs/reproducibility/artifact-manifest.md`
- `docs/ai-use-log.md`
- `engineering-log.md`

## Suggested Canvas text-entry blurb

```text
Repository: https://github.com/liangzixuan/cisc-699

This Hard Stop 5 package focuses on artifact hardening and reproducibility. It
adds a reviewer setup path, .env.example, reproducibility runbook, environment
and data/redistribution notes, artifact manifest, make repro-audit, and make
package-artifact. The submitted source package was unpacked into a fresh /tmp
directory and the documented smoke, test, validation, and reproducibility-audit
commands passed. Local validation reports local 12/12 passed plus API trace
passed. Docker/gVisor remain documented target-host checks.
```

## Recording reminder

Record a 5-7 minute walkthrough using `walkthrough-script.md`. Show:

- Repository structure and README setup path.
- `.env.example` and `docs/reproducibility/`.
- `make smoke`, `make test`, `make validate`, and `make repro-audit` evidence.
- The source package and clean-run output.
- Known limitations, especially Docker/gVisor target-host dependency.

