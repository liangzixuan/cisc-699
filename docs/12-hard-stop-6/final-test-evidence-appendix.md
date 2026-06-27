# SafeExec Final Test Evidence Appendix

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from
> repository command outputs and evidence files. AI-drafted, student-revised.
> Full audit trail: `docs/ai-use-log.md`.

## Evidence Bundle Location

Fresh W12 evidence is stored in:

`docs/12-hard-stop-6/evidence/`

Primary command:

```bash
make final-evidence
```

This command runs smoke, unit/functional tests, local validation, reproducibility
audit, environment capture, and copies the prior Docker/gVisor target-host
summary evidence into the W12 evidence folder.

## Fresh Local Evidence Summary

| Check | Command | Result | Transcript |
|---|---|---:|---|
| Smoke execution | `make smoke` | PASS | `evidence/smoke-output.txt` |
| Unit/functional tests | `make test` | PASS | `evidence/unit-tests-output.txt` |
| Local validation | `python3 scripts/run_validation_workflow.py --output-dir docs/12-hard-stop-6/evidence --repeat 3` | PASS | `evidence/local-validation-output.txt` |
| Reproducibility audit | `python3 scripts/audit_reproducibility.py --output-dir docs/12-hard-stop-6/evidence` | PASS | `evidence/reproducibility-audit-output.txt` |

Local validation result:

```text
include_docker: False
all_passed: True
local: 12/12 passed
api_trace: passed
```

The local cases cover normal stdout, deterministic arithmetic, stderr plus
non-zero exit code, timeout handling, and a live local API trace.

## Target-Host Evidence Brought Forward

The W12 appendix references W8 target-host evidence because Docker and gVisor
are Linux target-host checks, not macOS checks. Copies are included in the W12
evidence folder:

- `w8-target-midpoint-summary.md`
- `w8-target-midpoint-summary.csv`
- `w8-target-runsc-version.txt`

Target-host summary:

| Backend | Passed / Total | Pass rate | Mean duration | Median duration | Maximum duration |
|---|---:|---:|---:|---:|---:|
| Local subprocess | 30 / 30 | 100.0% | 93.2 ms | 32.9 ms | 402.0 ms |
| Hardened Docker | 50 / 50 | 100.0% | 868.8 ms | 771.7 ms | 1985.4 ms |
| gVisor (`runsc`) | 49 / 50 | 98.0% | 1361.8 ms | 1327.5 ms | 3167.2 ms |

Interpretation: Docker was stable on the current probe set. gVisor is
integrated and largely passing, but one `tmpfs_write_allowed` run timed out,
which means the final benchmark needs cold-start/warm-run timing separation.

## Reproducibility Evidence

W10 clean-run evidence is copied forward as:

- `w10-clean-run-output.txt`

It shows that the source package was built, unpacked under `/tmp`, and ran:

- `cp .env.example .env`
- `make smoke`
- `make test`
- local validation
- reproducibility audit

The W12 reproducibility audit passed and found no blocking reproducibility
findings.

## Evidence Limitations

- W12 fresh evidence is local/API evidence; it does not rerun Docker/gVisor on
  the macOS authoring machine.
- Docker/gVisor claims currently rely on the prior Ubuntu target-host evidence.
- The final HumanEval/MBPP subset and full adversarial suite remain the next
  evidence expansion step.
- The final report should avoid claiming final pass-rate thresholds until the
  expanded corpus and adversarial manifest have been run.

## Files to Cite in the Final Report

| Claim | Evidence file |
|---|---|
| Current local artifact still runs | `evidence/final-evidence-summary.txt` |
| Local validation/API trace passed | `evidence/validation-summary.txt`, `evidence/api-trace.json` |
| Unit tests passed | `evidence/unit-tests-output.txt` |
| Reproducibility audit passed | `evidence/reproducibility-audit.md` |
| Docker/gVisor target-host comparison exists | `evidence/w8-target-midpoint-summary.md` |
| Clean package can run outside working tree | `evidence/w10-clean-run-output.txt` |
| Runtime/toolchain context | `evidence/environment-snapshot.txt`, `evidence/environment-snapshot.json` |
