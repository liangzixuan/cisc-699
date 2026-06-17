# Implementation Sprint I Evidence Addendum

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from the
> W5 grading feedback, repository state, and generated command evidence.
> AI-drafted, student-revised. Full audit trail: `docs/ai-use-log.md`.

**Student:** Zixuan Liang  
**Course:** CISC 699-50-A-2026/Summer - Applied Project in Computer Information Science  
**Project:** SafeExec - Hardened Python Execution Sandbox for LLM Agent Tool-Use  
**Advisor:** Prof. Khalid Lateef  
**Instructor:** Dr. Majid Shaalan  
**Revision date:** 2026-06-17  

## 1. Purpose of This Addendum

The original W5 check-in accurately described the implementation baseline, but
the Canvas upload did not include several supporting artifacts referenced in
the PDF. This addendum makes the baseline independently verifiable by attaching
the repository link, commit/tag, setup files, repository snapshot, git log,
smoke/test outputs, architecture notes, changelog, risk log, engineering log,
and AI-use log.

## 2. Repository and Version Baseline

| Item | Value |
|---|---|
| Repository URL | https://github.com/liangzixuan/cisc-699 |
| Branch | `main` |
| W5 baseline commit | `3475ccf` |
| W5 baseline tag | `w5-baseline` |
| Commit subject | `Add W5 implementation sprint baseline` |
| Evidence file | `git-log-w5.txt` |

Git-log excerpt:

```text
3475ccf (tag: w5-baseline) Add W5 implementation sprint baseline
b5b2702 Add W4 design review package
a9d9e76 Record W2 proposal feedback
075bcc3 Record W3 advisor decisions
```

## 3. Evidence Matrix

| Feedback item | Evidence now attached |
|---|---|
| Repository or repository link missing | Repository URL, `repository-snapshot.txt`, `git-log-w5.txt` |
| Commit/tag/version-control baseline missing | Commit `3475ccf`, tag `w5-baseline`, `git-log-w5.txt` |
| Setup docs/files missing | `README.md`, `Makefile`, `pyproject.toml`, `requirements.txt`, `deploy/README.md` |
| Smoke/test output missing | `smoke-output-2026-06-17.txt`, `test-output-2026-06-17.txt`, excerpts below |
| Architecture notes missing | `architecture-notes.md` |
| Changelog/release note missing | `CHANGELOG.md` |
| Known-issues/risk log incomplete | `known-issues-risk-log.md` with severity, likelihood, owner, dates, and target resolution |
| AI-use log referenced but not uploaded | `docs/ai-use-log.md` |
| Engineering log referenced but not uploaded | `engineering-log.md` |

## 4. Setup and Reproducibility Evidence

The W5 baseline requires Python 3.11 or newer and has no third-party runtime
dependencies. The root `Makefile` provides the reproducible commands:

```bash
make smoke
make test
make api
```

The root `requirements.txt` intentionally records that W5 uses only the Python
standard library. The root `pyproject.toml` records the package name, version,
and Python requirement. `deploy/README.md` explains the API-shell wrapper and
states that the final Docker boundary is W6 work.

## 5. Smoke-Test Output

Fresh smoke output was captured on 2026-06-17 and is attached as
`smoke-output-2026-06-17.txt`.

```text
PYTHONPATH=src python3 scripts/smoke_safeexec.py
{
  "backend": "local",
  "contained": true,
  "containment_reason": "dev_subprocess_completed",
  "exit_code": 0,
  "status": "ok",
  "stderr": "",
  "stdout": "hello from safeexec sprint 1\n"
}
```

The `local` backend remains a development-only smoke path. It proves the
request/result/API/test contract is runnable; it does not prove security
containment.

## 6. Test Log Output

Fresh test output was captured on 2026-06-17 and is attached as
`test-output-2026-06-17.txt`.

```text
PYTHONPATH=src python3 -m unittest discover -s tests/functional -p 'test_*.py'
.....
----------------------------------------------------------------------
Ran 5 tests in 0.869s

OK
```

The tests cover local execution, timeout reporting, API response shape, Docker
hardening command controls, and gVisor runtime selection.

## 7. Risk and Issue Management

The original risk table was technically meaningful but too small for the rubric.
The revised `known-issues-risk-log.md` adds severity, likelihood, owner, status,
opened date, updated date, target resolution, and mitigation action. The most
important open implementation risk remains Docker/gVisor verification on the
Ubuntu droplet. The most important submission-process risk was the omitted
evidence upload; this addendum resolves that by making the evidence explicit.

## 8. Resubmission Attachment Checklist

If revision is allowed, submit this addendum together with the following
supporting artifacts:

- `Implementation-Sprint-I-Evidence-Addendum.pdf`
- `Implementation-Sprint-I-Evidence-Addendum.docx`
- `Implementation-Sprint-I-Check-in.pdf`
- `README.md`
- `Makefile`
- `pyproject.toml`
- `requirements.txt`
- `deploy/README.md`
- `evidence-index.md`
- `repository-snapshot.txt`
- `git-log-w5.txt`
- `smoke-output-2026-06-17.txt`
- `test-output-2026-06-17.txt`
- `known-issues-risk-log.md`
- `architecture-notes.md`
- `CHANGELOG.md`
- `docs/ai-use-log.md`
- `engineering-log.md`
