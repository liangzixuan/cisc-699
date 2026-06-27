# SafeExec Reproducibility Runbook

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from
> the current SafeExec repository and validation evidence. AI-drafted,
> student-revised. Full audit trail: `docs/ai-use-log.md`.

This runbook is the shortest path for a peer reviewer to reproduce the current
SafeExec artifact state.

## 1. Runtime assumptions

- Python 3.11 or newer.
- No required Python third-party packages for the current prototype.
- GNU Make is optional but recommended.
- Docker is required only for `docker` backend checks.
- gVisor `runsc` is required only for `gvisor` backend checks.

The local subprocess backend is for development smoke testing only. It is not a
security boundary and should not be used as containment evidence.

## 2. Fresh setup

```bash
git clone https://github.com/liangzixuan/cisc-699.git
cd cisc-699
python3 --version
cp .env.example .env
```

If `make` is available:

```bash
make smoke
make test
make validate
make repro-audit
```

Without `make`, use direct Python commands:

```bash
PYTHONPATH=src python3 scripts/smoke_safeexec.py
PYTHONPATH=src python3 -m unittest discover -s tests/functional -p 'test_*.py'
PYTHONPATH=src python3 scripts/run_validation_workflow.py --output-dir docs/10-hard-stop-5/evidence --repeat 3
PYTHONPATH=src python3 scripts/audit_reproducibility.py --output-dir docs/10-hard-stop-5/evidence
```

## 3. Container backend checks

On a Linux host with Docker:

```bash
docker pull python:3.11-slim
PYTHONPATH=src python3 scripts/run_validation_workflow.py --output-dir docs/10-hard-stop-5/evidence-target --repeat 3 --include-docker
```

For gVisor, `runsc` must be installed and registered as a Docker runtime. The
W8 target-host evidence used `runsc version release-20260511.0`.

## 4. Expected local results

The local reproducibility pass should show:

- `make smoke` prints a structured SafeExec result with `status: ok`.
- `make test` runs the functional test suite successfully.
- `make validate` reports local validation and API trace success.
- `make repro-audit` reports no blocking reproducibility-material findings.

## 5. Known limitations

- Local macOS Docker is not available in the student's current authoring
  environment, so Docker/gVisor evidence is collected on the Ubuntu target host.
- The Ubuntu target host previously lacked `make`; direct Python commands are
  documented above as equivalent.
- Full HumanEval/MBPP and adversarial-suite evidence is still future work. The
  current runbook reproduces the prototype and current validation harness.

