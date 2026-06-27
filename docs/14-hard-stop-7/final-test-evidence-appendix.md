# SafeExec Final Test Evidence Appendix

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from
> final evidence command outputs. AI-drafted, student-revised. Full audit
> trail: `docs/ai-use-log.md`.

## Evidence Location

Fresh final evidence is stored in:

`docs/14-hard-stop-7/evidence/`

Primary command:

```bash
PYTHONPATH=src python3 scripts/run_final_evidence.py --output-dir docs/14-hard-stop-7/evidence --repeat 3
```

## Final Local Evidence Summary

| Check | Result | Transcript |
|---|---:|---|
| Smoke execution | PASS | `evidence/smoke-output.txt` |
| Unit/functional tests | PASS | `evidence/unit-tests-output.txt` |
| Local validation/API trace | PASS | `evidence/validation-summary.txt` |
| Reproducibility audit | PASS | `evidence/reproducibility-audit.md` |

The local validation workflow passed 12/12 local records and the API trace.

## Target-Host Evidence Brought Forward

Docker and gVisor are target-host checks, not local macOS checks. The final
package therefore carries forward the target-host evidence from W8:

| Backend | Passed / Total | Pass rate | Mean duration | Median duration | Maximum duration |
|---|---:|---:|---:|---:|---:|
| Local subprocess | 30 / 30 | 100.0% | 93.2 ms | 32.9 ms | 402.0 ms |
| Hardened Docker | 50 / 50 | 100.0% | 868.8 ms | 771.7 ms | 1985.4 ms |
| gVisor (`runsc`) | 49 / 50 | 98.0% | 1361.8 ms | 1327.5 ms | 3167.2 ms |

The gVisor miss was a timeout on one tmpfs write case. This is interpreted as
a timing-methodology limitation requiring cold-start/warm-run separation, not
as a demonstrated sandbox escape.

## Reproducibility Evidence

The final package includes:

- `.env.example`
- `docs/reproducibility/runbook.md`
- `docs/reproducibility/environment.md`
- `docs/reproducibility/data-and-redistribution.md`
- `docs/reproducibility/artifact-manifest.md`
- `scripts/audit_reproducibility.py`
- `scripts/package_final_submission.py`
- `safeexec-final-artifact-package.zip`

The final reproducibility audit passed with no blocking findings.

## Evidence Limitations

- The final local evidence is local/API evidence only.
- Docker/gVisor evidence is copied from the target-host benchmark run.
- HumanEval/MBPP and adversarial-corpus expansion remain future work at the
  originally planned scale.
- The final report should not claim production security or general sandbox
  safety.
