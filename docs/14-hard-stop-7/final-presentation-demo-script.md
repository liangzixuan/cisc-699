# SafeExec Final Presentation and Demo Script

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from
> the final report, final deck, and evidence bundle. AI-drafted,
> student-revised. Full audit trail: `docs/ai-use-log.md`.

Target length: 8-10 minutes.

## 1. Opening

This is my final CISC 699 presentation for SafeExec, a hardened,
threat-modeled Python execution sandbox for LLM-agent tool use.

The project focuses on the point where generated text becomes process
execution. My goal was not to build a production platform. My goal was to build
an inspectable artifact that can run code, apply visible controls, return
structured evidence, and support a transparent Docker-versus-gVisor comparison.

## 2. Problem and Motivation

LLM agents can plan, call tools, and execute generated code. That is useful,
but it creates a systems-security boundary. If generated code runs directly on
the host, prompt injection, model error, or excessive agency can become file
access, network egress, or resource exhaustion.

SafeExec treats generated Python as untrusted and asks: can the executor make
that boundary observable?

## 3. Architecture

Show the architecture slide.

The system uses one request model and one result model:

```text
ExecutionRequest -> service -> local | Docker | gVisor -> ExecutionResult
```

The local backend is a development smoke path only. The containment-relevant
paths are hardened Docker and gVisor through `runsc`.

## 4. Artifact Walkthrough

Show repository files:

- `src/safeexec/models.py`
- `src/safeexec/service.py`
- `src/safeexec/backends/docker.py`
- `src/safeexec/api/server.py`
- `scripts/run_validation_workflow.py`
- `scripts/run_final_evidence.py`

Explain that the implementation is compact on purpose. It is easier to audit
and easier to connect to the evidence.

## 5. Evidence

Open `docs/14-hard-stop-7/evidence/final-evidence-summary.txt`.

Point out:

- smoke: PASS
- unit tests: PASS
- local validation: PASS
- reproducibility audit: PASS

Open `docs/14-hard-stop-7/evidence/validation-summary.txt`.

Point out:

- local: 12/12 passed
- API trace: passed

## 6. Docker and gVisor Results

Open `docs/14-hard-stop-7/evidence/w8-target-midpoint-summary.md`.

Summarize:

- local subprocess: 30/30,
- hardened Docker: 50/50,
- gVisor: 49/50.

The single gVisor miss was a timeout on one tmpfs write case. I report that as
a timing-methodology limitation rather than hiding it.

## 7. Reproducibility and Package

Show:

- `docs/reproducibility/runbook.md`
- `.env.example`
- `safeexec-final-artifact-package.zip`
- `final-evidence.zip`

Explain that earlier feedback emphasized verifiable evidence, so the final
package includes direct command transcripts and packaged source, not just a
narrative report.

## 8. Limitations

State the limits clearly:

- local backend is not a security boundary,
- Docker/gVisor evidence requires the target host,
- the original full HumanEval/MBPP and adversarial-suite targets remain future
  work,
- the API is not production hardened.

These limits are part of the report, not hidden from it.

## 9. Closing

The final contribution is an evidence-oriented sandbox artifact. SafeExec shows
graduate-level design, implementation, reproducibility, and evaluation
discipline for LLM-agent Python execution. It is not a finished commercial
sandbox, but it is a working, inspectable, and defensibly documented capstone
artifact.
