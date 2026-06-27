# SafeExec Draft Report, Deck, and Final Test Evidence

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from
> repository artifacts and fresh W12 evidence. AI-drafted, student-revised.
> Full audit trail: `docs/ai-use-log.md`.

**Course:** CISC 699 Applied Project in Computer Information Sciences  
**Student:** Zixuan Liang  
**Advisor:** Prof. Khalid Lateef  
**Instructor:** Dr. Majid Shaalan  
**Assignment:** 12 Hard Stop 6: Draft Report, Deck, and Final Test Evidence  
**Prepared:** 2026-06-26

## 1. Package Purpose

This package connects the three required streams for Hard Stop 6:

1. a near-final technical report draft,
2. a presentation/demo deck and walkthrough script, and
3. final-test evidence that supports the report and deck claims.

The main story is consistent across all three: SafeExec has moved from a
scaffold into a reproducible, testable sandbox artifact. The current evidence
supports the claim that the API/result path, local validation, reproducibility
audit, and Docker/gVisor benchmark harness are functioning. The remaining work
is corpus depth and final benchmark refresh, not a change in project direction.

## 2. Current Draft Report Status

Primary draft report file:

`near-final-technical-report-draft.md`

The draft now includes:

- abstract and problem statement,
- related-work synthesis,
- approved scope and requirements,
- system design and implementation status,
- evaluation methodology,
- current results and interpretation,
- ethics/security/privacy discussion,
- limitations and final-week work plan,
- reference list aligned to the W3 literature brief.

This draft is not yet the W14 final report. The remaining report work is to
insert the final HumanEval/MBPP subset table, expanded adversarial results,
final Docker/gVisor benchmark tables, and final demo screenshots or transcript.

## 3. Presentation and Demo Readiness

Primary deck:

`SafeExec-Draft-Report-and-Demo-Deck.pptx`

Primary walkthrough script:

`walkthrough-script.md`

The deck follows the same report arc:

1. problem and project claim,
2. artifact architecture,
3. current implementation,
4. evidence collected,
5. Docker/gVisor findings,
6. limitations and remaining work,
7. final-week plan.

The deck intentionally avoids adding claims that do not appear in the report.
Every numeric claim in the deck is traceable to W8, W10, or W12 evidence files.

## 4. Final Test Evidence Summary

Fresh W12 evidence was generated with:

```bash
make final-evidence
```

Summary:

| Evidence stream | Result | File |
|---|---:|---|
| Smoke execution | PASS | `evidence/smoke-output.txt` |
| Unit/functional tests | PASS | `evidence/unit-tests-output.txt` |
| Local validation/API trace | PASS | `evidence/validation-summary.txt` |
| Reproducibility audit | PASS | `evidence/reproducibility-audit.md` |
| Environment snapshot | Captured | `evidence/environment-snapshot.txt` |

The local validation workflow passed 12/12 local records and the API trace.
The reproducibility audit passed with no blocking findings.

## 5. Evidence Brought Forward

The W12 folder includes copies of important prior evidence so the reviewer can
see the full evidence chain in one package:

- W8 target-host Docker/gVisor summary:
  `evidence/w8-target-midpoint-summary.md`
- W8 target-host CSV summary:
  `evidence/w8-target-midpoint-summary.csv`
- W8 runsc version:
  `evidence/w8-target-runsc-version.txt`
- W10 clean package run:
  `evidence/w10-clean-run-output.txt`

The most important target-host result remains:

| Backend | Passed / Total | Pass rate |
|---|---:|---:|
| Local subprocess | 30 / 30 | 100.0% |
| Hardened Docker | 50 / 50 | 100.0% |
| gVisor (`runsc`) | 49 / 50 | 98.0% |

## 6. Interpretation and Midpoint-to-Final Adjustment

The evidence supports the artifact's basic technical maturity:

- the API/result schema is stable enough for repeatable validation;
- Docker hardening is exercised on a real target host;
- gVisor is integrated through `runsc`;
- local validation and reproducibility checks are repeatable;
- the clean-run package path is documented and tested.

The evidence does not yet justify final headline claims about the complete
functional corpus or adversarial containment thresholds. Those are final-week
targets. The report and deck therefore present the current results as a strong
engineering baseline plus a clear final evidence plan.

## 7. Revision Responsiveness

Earlier implementation-sprint feedback criticized missing verifiable evidence.
This package responds directly:

- evidence files are included rather than merely referenced;
- command transcripts are in `evidence/`;
- environment snapshots are submitted;
- reproducibility audit and clean-run evidence are included;
- report/deck/checklist all point to the same files.

## 8. Submission Contents

Recommended Canvas upload:

- `Draft-Report-Deck-Final-Test-Evidence.docx`
- `Draft-Report-Deck-Final-Test-Evidence.pdf`
- `near-final-technical-report-draft.md`
- `final-test-evidence-appendix.md`
- `SafeExec-Draft-Report-and-Demo-Deck.pptx`
- `walkthrough-script.md`
- `canvas-submission-checklist.md`
- the full `evidence/` folder or a zip of it
- `docs/ai-use-log.md`

## 9. Remaining Work Before Final Submission

1. Finish HumanEval/MBPP subset manifest and license/provenance table.
2. Expand adversarial suite to the approved count/category target.
3. Re-run Docker/gVisor benchmark on the Ubuntu target host.
4. Separate cold-start and warm-run timing in final performance tables.
5. Add final results to the report and deck.
6. Record the final walkthrough/demo.
7. Rebuild final reproducibility package and rerun `make final-evidence`.
