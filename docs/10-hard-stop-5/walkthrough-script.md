# W10 Walkthrough Script: Artifact Hardening and Reproducibility

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app).
> AI-drafted, student-revised. Full audit trail: `docs/ai-use-log.md`.

Target length: 5-7 minutes.

## 0:00-0:45 — Purpose

This walkthrough is for Hard Stop 5, Artifact Hardening and Reproducibility.
The goal is to show that SafeExec is not only runnable on my machine, but has a
clear handoff path for another technical reader.

## 0:45-1:45 — Repository and setup entry point

Show `README.md`.

Point out:

- Fresh reviewer setup commands.
- `make smoke`, `make test`, `make validate`, `make repro-audit`.
- The warning that local subprocess is only a development backend, not a
  containment boundary.

## 1:45-2:45 — Configuration and reproducibility docs

Show `.env.example` and `docs/reproducibility/`.

Explain:

- No secrets or external API credentials are required.
- `runbook.md` gives direct commands if `make` is unavailable.
- `environment.md` names Python, Docker, and gVisor assumptions.
- `data-and-redistribution.md` explains that current tests are
  student-authored and that HumanEval/MBPP require provenance/license notes
  later.
- `artifact-manifest.md` maps source, tests, scripts, and docs.

## 2:45-4:00 — Evidence commands

Show files in `docs/10-hard-stop-5/evidence/`.

Summarize:

- `smoke-output.txt`: local execution returns `status: ok`.
- `test-output.txt`: functional suite passes with 7 tests.
- `validation-summary.txt`: local validation passes 12/12 plus API trace.
- `reproducibility-audit.md`: required paths, README markers, Make targets,
  and dependency policy pass.

## 4:00-5:15 — Clean package run

Show `safeexec-reproducibility-package.tar.gz` and
`evidence/clean-run-output.txt`.

Explain that the clean run used the package, unpacked it under `/tmp`, copied
`.env.example` to `.env`, and reran the documented commands. This is the
closest current evidence to a peer-reviewer handoff.

## 5:15-6:15 — Limitations and next steps

Be explicit:

- Local macOS does not provide Docker/gVisor evidence.
- Docker/gVisor remain target-host checks on Ubuntu.
- Full HumanEval/MBPP and adversarial suite are not final yet.
- Next hardening work is Python 3.11 target-host consistency, cold/warm
  benchmark separation, and corpus provenance.

## 6:15-6:45 — Close

Close by saying: the artifact is not final, but setup, validation, packaging,
and limitations are now explicit enough that another reader can reproduce the
current state and see exactly what remains.

