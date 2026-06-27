# SafeExec W12 Walkthrough Script

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from
> the W12 package and evidence files. AI-drafted, student-revised. Full audit
> trail: `docs/ai-use-log.md`.

Target length: 6-8 minutes.

## 1. Opening and Project Claim

This is the Hard Stop 6 draft report, deck, and final test evidence package for
SafeExec, my CISC 699 applied project. The project builds a hardened,
threat-modeled Python execution sandbox for LLM-agent tool use.

The central claim is not simply that the service can run Python. The claim is
that SafeExec can make sandbox behavior measurable: which backend ran, which
limits were applied, what output was returned, whether containment behavior was
observed, and whether another reader can reproduce the evidence.

## 2. Show the Report Draft

Open `near-final-technical-report-draft.md` or the generated DOCX/PDF.

Point out:

- abstract and problem statement,
- related work and threat model,
- implementation status,
- evaluation methodology,
- current results,
- limitations and final-week plan.

Emphasize that the report is near-final but not final. The final corpus and
adversarial results still need to be inserted after the last target-host run.

## 3. Show the Architecture

Use the deck architecture slide or explain from the report:

```text
ExecutionRequest
  -> service layer
    -> local backend | hardened Docker | gVisor/runsc
      -> ExecutionResult
```

Make clear that the local backend is a development smoke path, not a security
boundary. Docker and gVisor are the containment-relevant backends.

## 4. Show Fresh W12 Evidence

Open `docs/12-hard-stop-6/evidence/final-evidence-summary.txt`.

Read the key result:

```text
all_passed: True
smoke: PASS
unit-tests: PASS
local-validation: PASS
reproducibility-audit: PASS
```

Then open `validation-summary.txt` and show:

```text
local: 12/12 passed
api_trace: passed
```

Explain that this is the fresh local evidence for W12.

## 5. Show Docker/gVisor Evidence

Open `docs/12-hard-stop-6/evidence/w8-target-midpoint-summary.md`.

Explain that Docker/gVisor runs are target-host evidence because they require
the Ubuntu Docker/gVisor environment. Summarize:

- local subprocess: 30/30,
- hardened Docker: 50/50,
- gVisor: 49/50.

The gVisor miss was a timeout on one tmpfs write case, so the final benchmark
needs clearer cold-start versus warm-run timing. This is reported as a
methodology adjustment, not hidden.

## 6. Show Reproducibility Evidence

Open `docs/12-hard-stop-6/evidence/reproducibility-audit.md` and
`docs/12-hard-stop-6/evidence/w10-clean-run-output.txt`.

Explain that the W10 feedback path emphasized verifiable evidence. This package
includes the commands and outputs directly:

- README/runbook setup path,
- `.env.example`,
- source package builder,
- reproducibility audit,
- clean unpacked package run.

## 7. Show the Deck

Open `SafeExec-Draft-Report-and-Demo-Deck.pptx`.

Walk through the deck quickly:

1. project claim,
2. architecture,
3. implementation surface,
4. evidence collected,
5. Docker/gVisor result,
6. limitations,
7. final-week plan.

Emphasize that the deck and report use the same numbers and limitations.

## 8. Closing

Close by saying:

SafeExec is technically on track. The artifact is running, documented,
reproducible locally, and supported by earlier Docker/gVisor target-host
evidence. The final work is not to add a large new feature; it is to complete
the functional/adversarial corpora, rerun the target-host benchmark, and update
the final report and deck with final evidence.
