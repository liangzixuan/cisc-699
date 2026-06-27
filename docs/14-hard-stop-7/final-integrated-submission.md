# SafeExec Final Integrated Submission

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from
> the final report, artifact package, evidence bundle, and presentation deck.
> AI-drafted, student-revised. Full audit trail: `docs/ai-use-log.md`.

**Assignment:** 14 Hard Stop 7: Final Integrated Submission and Presentation/Demo  
**Student:** Zixuan Liang  
**Advisor:** Prof. Khalid Lateef  
**Instructor:** Dr. Majid Shaalan  
**Prepared:** 2026-06-27

## Package Summary

This final integrated package submits the SafeExec technical report,
computational artifact, evidence bundle, and presentation/demo materials as one
coherent capstone submission.

SafeExec is a hardened, threat-modeled Python execution sandbox for LLM-agent
tool use. The implementation includes a structured execution model, local
development backend, hardened Docker command path, gVisor `runsc` path, API
shell, validation scripts, reproducibility docs, and final artifact package.

## Final Submission Contents

| Required item | Submitted file(s) |
|---|---|
| Final report | `Final-Technical-Report.docx`, `Final-Technical-Report.pdf`, `final-technical-report.md` |
| Computational artifact package | `safeexec-final-artifact-package.zip` |
| Final evidence bundle | `final-evidence.zip`, `evidence/` |
| Presentation/demo deck | `Final-Presentation-and-Demo-Deck.pptx`, `Final-Presentation-and-Demo-Deck.pdf` |
| Walkthrough/demo script | `final-presentation-demo-script.md` |
| Release/archive notes | `final-release-notes.md` |
| AI-use disclosure | `docs/ai-use-log.md` |

## Technical Result

Fresh final evidence passed:

- smoke execution,
- unit/functional tests,
- local validation/API trace,
- reproducibility audit.

The strongest Docker/gVisor target-host evidence remains:

| Backend | Passed / Total | Pass rate |
|---|---:|---:|
| Local subprocess | 30 / 30 | 100.0% |
| Hardened Docker | 50 / 50 | 100.0% |
| gVisor (`runsc`) | 49 / 50 | 98.0% |

## Main Limitation

The final package is honest about the largest remaining gap: the HumanEval/MBPP
functional subset and expanded adversarial suite are not yet at the original
stretch-target scale. The submitted artifact is still runnable, reproducible,
and evidence-backed, but it should not be described as a production sandbox or
as proof of general adversarial safety.

## Reviewer Navigation

1. Read `Final-Technical-Report.pdf`.
2. Inspect `final-test-evidence-appendix.md` for the evidence map.
3. Open `safeexec-final-artifact-package.zip` for source, tests, scripts,
   reproducibility docs, and evidence files.
4. Review `Final-Presentation-and-Demo-Deck.pdf` or `.pptx`.
5. Use `final-presentation-demo-script.md` to record or review the walkthrough.
