# Hard Stop 3: Early Implementation Validation Package

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) from
> the W6 Canvas assignment screenshot, committed SafeExec code, and generated
> local/droplet validation logs. AI-drafted, student-revised. Full audit trail:
> `docs/ai-use-log.md`.

**Student:** Zixuan Liang  
**Course:** CISC 699-50-A-2026/Summer - Applied Project in Computer Information Science  
**Project:** SafeExec - Hardened Python Execution Sandbox for LLM Agent Tool-Use  
**Advisor:** Prof. Khalid Lateef  
**Instructor:** Dr. Majid Shaalan  
**Submission date:** 2026-06-17  
**Repository:** https://github.com/liangzixuan/cisc-699  
**Validation harness commit:** `674fa58`  

## 1. Validation Objective

Hard Stop 3 asks whether the project is technically alive enough to support
meaningful evidence collection before the midpoint review. For SafeExec, the
current validation target is the deepest implemented path available in W6:

- request/result models and backend selection;
- local development backend with timeout and structured output;
- stdlib JSON `POST /execute` API shell;
- Docker backend using the hardened command shape;
- gVisor backend using Docker runtime `runsc`;
- repeatable validation workflow that emits JSON and text evidence.

This is still early validation, not final performance or security evaluation.
The results show that the technical path now runs repeatedly on the target
Ubuntu droplet, while also identifying environment issues that must be cleaned
up before the midpoint demo.

## 2. Implemented Workflow

| Layer | Implemented path | Evidence |
|---|---|---|
| Local service path | `ExecutionRequest` -> backend selection -> `LocalSubprocessBackend` -> `ExecutionResult` | `evidence/validation-summary.txt`, `evidence-target-rerun/validation-summary.txt` |
| API path | In-process HTTP server handles `POST /execute` and returns structured JSON | `api-trace.json` in local and target evidence directories |
| Docker path | `DockerBackend` runs `python:3.11-slim` with no network, non-root user, read-only rootfs, dropped capabilities, no-new-privileges, memory/CPU/PID limits, and tmpfs workspace | `evidence-target-rerun/validation-summary.txt` |
| gVisor path | Same Docker command with `--runtime runsc` | `evidence-target-rerun/validation-summary.txt` |
| Repeatability | Three iterations per case for local, Docker, and gVisor validation | `validation-results.json` and `validation-summary.txt` |

## 3. Environment and Toolchain Snapshot

| Environment | Key facts | Interpretation |
|---|---|---|
| Local authoring machine | macOS/Darwin ARM64, Python 3.14.5. Docker CLI installed but daemon unavailable. | Suitable for code authoring, unit tests, local/API validation. Not suitable for container evidence in this session. |
| Target validation host | Ubuntu 22.04 droplet, Linux 5.15.0-179-generic x86_64, Docker 29.5.0, `runsc` release-20260511.0. | Official environment for Docker/gVisor validation. |
| Target host caveats | Host Python is 3.10.12 and `make` is not installed. Container execution uses `python:3.11-slim`. | The backend path validates Python 3.11 execution, but the host harness should be moved to Python 3.11 or a dev container before W7. |

Local Docker output confirms the local daemon limitation:

```text
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

Target environment excerpt:

```text
system: Linux 5.15.0-179-generic x86_64
python: 3.10.12
git_head: 674fa58f5a21b35a7121fdfcf990725a761cce23
docker_client: ok Client: Docker Engine - Community
runsc: ok runsc version release-20260511.0
make: not-ready [Errno 2] No such file or directory: 'make'
```

## 4. Validation Cases

| Case | Purpose | Expected result |
|---|---|---|
| `hello_stdout` | Basic stdout path. | Status `ok`, exact stdout. |
| `deterministic_arithmetic` | Deterministic computation. | Status `ok`, stdout `285`. |
| `stderr_and_exit_code` | Error-channel and nonzero exit handling. | Status `error`, exit code `3`, exact stderr. |
| `timeout_control` | Wall-time containment in local backend. | Status `timeout`, containment reason `wall_timeout`. |
| `container_hello` | Docker/gVisor container execution and non-root UID output. | Status `ok`. |
| `network_disabled_probe` | Early no-network validation for Docker/gVisor. | Status `ok` with connection failure output, not `network-open`. |
| `api_trace` | `POST /execute` request/response path. | HTTP 200 and stdout `api validation`. |

## 5. Results

### Local validation

Local tests passed:

```text
Ran 7 tests in 1.356s
OK
```

Local validation workflow passed local service and API checks:

```text
include_docker: False
all_passed: True
- local: 12/12 passed
- api_trace: passed
```

### Target-host validation, first run

The first target-host Docker/gVisor validation run found one reproducibility
defect:

```text
include_docker: True
all_passed: False
- local: 12/12 passed
- docker: 5/6 passed
- gvisor: 6/6 passed
- api_trace: passed
docker::container_hello#1 FAIL status=timeout exit=None reason=wall_timeout
```

The failure was not a program-correctness failure. It occurred because the first
Docker run spent the timeout window pulling `python:3.11-slim`. The image pull
completed, and subsequent Docker cases passed.

### Target-host validation, clean rerun

After the image was cached, the clean target-host rerun passed:

```text
include_docker: True
all_passed: True
- local: 12/12 passed
- docker: 6/6 passed
- gvisor: 6/6 passed
- api_trace: passed
```

The cached image evidence is:

```text
python:3.11-slim   ae52c5bef62a   188MB   47.7MB
sha256:ae52c5bef62a6bdd42cd1e8dffef86b9cd284bde9427da79839de7a4b983e7ca amd64 linux
```

## 6. Interpretation

The validation supports three claims:

1. The SafeExec execution contract is now repeatable. The same validation
   harness emits structured JSON and text summaries on both the local authoring
   machine and the Ubuntu target host.
2. The early Docker and gVisor paths are technically alive. Both backends ran
   sample Python programs under the intended command shape and passed the
   network-disabled probe after the base image was cached.
3. The project is ready for W7 expansion, but not for final security claims.
   The current validation is smoke/integration evidence. It is not yet the full
   functional corpus, adversarial benchmark, or performance study promised for
   W8-W14.

The most important finding is the image-pull timeout. This is a practical
reproducibility issue: a timed validation run should not include dependency
download time unless the experiment is explicitly measuring cold setup. The W7
workflow should pre-pull and record image digests before timed tests.

## 7. Defects, Bottlenecks, and Workarounds

| Finding | Evidence | Status | Next action |
|---|---|---|---|
| First Docker run timed out during image pull. | `evidence-target/validation-summary.txt` | Mitigated | Pre-pull `python:3.11-slim` and record digest before validation. |
| Local Docker daemon unavailable on macOS. | `evidence/local-docker-version.txt` | Accepted limitation | Use Ubuntu droplet as official container validation host. |
| Target host lacks `make`. | `evidence-target/environment-snapshot.txt` | Open | Install `make` or document direct Python equivalents. |
| Target host Python is 3.10.12. | `evidence-target/environment-snapshot.txt` | Open | Install Python 3.11 or run the harness in a Python 3.11 dev container. |
| Functional/adversarial corpora are still small. | Validation case list | Open | Add HumanEval/MBPP manifest and program-level adversarial cases. |

## 8. Readiness for Midpoint Review

The project is on track for midpoint review if W7 focuses on evidence growth
rather than new documentation. The immediate W7 targets are:

1. make target-host setup reproducible with `make` or equivalent documented
   commands;
2. pre-pull and pin the Python container image digest;
3. add the first functional corpus manifest and at least 30 runnable programs;
4. add initial adversarial programs for resource, network, process, filesystem,
   and environment probes;
5. capture a short midpoint demo showing local, Docker, and gVisor paths through
   the same validation harness.

## 9. Submitted Evidence

| Evidence file | Meaning |
|---|---|
| `evidence/environment-snapshot.txt` | Local authoring environment and Docker-daemon limitation. |
| `evidence/local-test-output.txt` | Local unit-test output. |
| `evidence/local-validation-output.txt` | Local validation command output. |
| `evidence/validation-summary.txt` | Local/API validation summary. |
| `evidence-target/environment-snapshot.txt` | Ubuntu droplet environment snapshot. |
| `evidence-target/target-test-output.txt` | Target-host unit-test output. |
| `evidence-target/validation-summary.txt` | First Docker/gVisor run with image-pull timeout. |
| `evidence-target/docker-image-python311.txt` | Cached image ID/digest evidence. |
| `evidence-target-rerun/validation-summary.txt` | Clean repeated Docker/gVisor validation run. |
| `evidence-target-rerun/validation-results.json` | Machine-readable target-host validation results. |
| `known-issues-risk-log.md` | Updated defect/risk tracker. |
