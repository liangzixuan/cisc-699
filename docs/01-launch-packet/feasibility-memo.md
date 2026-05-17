# Feasibility Memo

## 1. Data availability

The project does not consume a large dataset. The "data" required falls into three categories:

**(a) Functional test corpus.** A modest set of correct Python programs whose output the sandbox must reproduce faithfully. Candidate sources:
- HumanEval (Chen et al., 2021; MIT license per upstream) — 164 hand-written Python programming problems with reference solutions.
- MBPP (Austin et al., 2021; CC-BY-4.0 per the HuggingFace dataset card) — 974 entry-level Python programming problems.
- Hand-authored programs covering Python stdlib features the suite needs to exercise (`json`, `math`, `re`, `itertools`, `dataclasses`, `pathlib`, `unicodedata`, etc.).

A reasonable W1 plan is to take ~60 programs from HumanEval and ~40 hand-authored programs targeting stdlib coverage, totaling ≥100 functional cases. Both candidate corpora are redistributable under permissive licenses.

**(b) Adversarial test corpus.** This is the project's central contribution; it is *authored* rather than sourced. The taxonomy will be finalized in W3 design work but currently anticipates these categories: resource exhaustion (CPU, memory, fork bombs), file-descriptor exhaustion, attempted persistence across sessions, host-environment enumeration, attempted egress (DNS, sockets, ICMP), syscall abuse (e.g., attempted `ptrace`, `mount`, `unshare`), attempted privilege escalation (mirroring patterns from runc CVE-2019-5736, runc CVE-2024-21626), and "looks-benign-but-exfils" cases (e.g., timing channels through cache behavior, attempted exfiltration via `/proc` enumeration). Target: ≥40 programs across ≥6 categories.

**(c) Reference-agent demo input.** A small example workload for the W14 demo: a one-paragraph task description that exercises the agent → sandbox → result loop end-to-end. Authored, not sourced.

| Risk | Mitigation |
|---|---|
| HumanEval / MBPP license drift | Re-verify license texts at the moment of redistribution. Default to hand-authored corpus if license becomes uncertain. |
| Adversarial corpus regarded as security research that triggers ethics-review concerns | All adversarial programs target *the project's own sandbox*, not external systems; framing in the report makes this explicit. |

Redistributing a subset of HumanEval/MBPP inside this repository under their stated upstream licenses is acceptable.

## 2. Compute needs

**Development environment.** A laptop is adequate for service development; a Linux VM is required for the runtime tests because both isolation back-ends target Linux. Three viable hosting options for the runtime test VM:

| Option | Indicative cost (May 2026, USD) | Notes |
|---|---|---|
| Hetzner CCX13 (AMD, 2 vCPU, 8 GB, x86-64) | ~$7–9/mo | Cheapest credible production-grade x86-64 Linux VM; supports nested virtualization for Firecracker stretch. |
| DigitalOcean Premium AMD Droplet (2 vCPU, 4 GB) | ~$24/mo | More US-region availability, simpler billing for academic use. |
| AWS EC2 t3.medium (2 vCPU, 4 GB) | ~$30/mo on-demand, less spot | Most expensive of the three; only worth it if AWS credits are available. |
| Local Linux box on student's hardware | $0 marginal | Best if available; eliminates rental cost; performance numbers may not be reproducible by graders on different hardware. |

Across 14 weeks of intermittent use (one host running roughly 60% of the term), a cloud bill of **~$50–$100** is realistic for either Hetzner or a small AWS spot setup. *All prices are indicative based on publicly listed rates and must be re-verified at signup.*

**Reference-agent demo.** Uses the Anthropic Claude API; budget envelope is *low tens of dollars* for the full term given the demo is small (≤50 LOC, run during development and recorded once for submission). Caching transcripts and using a cheaper model (Claude Haiku) during development reduces this further. *Specific per-token pricing must be re-verified at signup.*

**Performance-benchmark experiments.** Same VM as above; benchmarks are I/O-light and short-running. Roughly 4–8 hours of wall-clock VM time per benchmark sweep, run perhaps three times across W8–W10 (initial, after gVisor lands, post-tuning). No additional compute beyond the rental.

**Total compute/API envelope across 14 weeks:** ~$100–$200 cloud + ~$30–$50 API = **~$150–$250 expected**, with the charter's ~$200–$400 ceiling preserved as buffer.

| Risk | Mitigation |
|---|---|
| Cloud provider pricing changes mid-term | Lock in a credit-funded prepaid balance; switch providers at month boundary if needed. |
| Benchmark non-reproducible due to noisy-neighbor VMs | Run benchmarks on a dedicated CPU instance for the final sweep; document hardware in the report. |
| HU lab access blocks installing gVisor (`runsc` requires root or apt-source addition) | Default to personal cloud VM; raise as the W2 supervisor question if HU lab is preferred path. |

Pick a compute provider DigitalOcean and set up the account. Verify HU lab availability by end of W2.

## 3. Software dependencies

Core stack (all open-source, all installable on Ubuntu 22.04 LTS or 24.04 LTS):

| Component | Version target | Source / install path |
|---|---|---|
| Ubuntu LTS host | 22.04 or 24.04 (kernel ≥5.15) | Cloud image or local install |
| Docker Engine | 24.x or 25.x | docker.com apt repo |
| gVisor (`runsc`) | latest stable | gvisor.dev apt repo: `storage.googleapis.com/gvisor/releases release main` |
| Python | 3.11.x | apt `python3.11` + `python3.11-venv` |
| FastAPI | 0.110+ | pip |
| uvicorn | 0.29+ | pip |
| pytest | 8.x | pip |
| pytest-benchmark *or* hyperfine | latest | pip / apt |
| anthropic (SDK) | 0.30+ | pip (demo only) |
| seccomp-tools | latest | gem / apt (debugging only) |
| strace / bpftrace | apt versions | debugging adversarial-suite failures |

All Python dependencies will be pinned in `requirements.txt` and a lockfile (likely `uv.lock` or `pip-tools` output) by end of W5. All apt dependencies will be enumerated in `deploy/setup.sh` so the reproducibility setup is a single script invocation.

**Potential dependency risks.**
- gVisor releases new versions roughly monthly; pin to a specific `runsc` release at W7 and freeze for the rest of the term.
- Docker Engine kernel-feature compatibility: confirm the host kernel supports `cgroups v2` (default on Ubuntu 22.04+) — required for the cgroup-based memory/PID limits.
- AppArmor vs. SELinux: Ubuntu defaults to AppArmor; the hardened-Docker back-end will ship an AppArmor profile. If the host is RHEL/Rocky/Alma the project would need an SELinux profile instead. Decision: Ubuntu only for this project.

Confirmed Ubuntu 22.04 as the target host.

## 4. Deployment expectations

The artifact is **not** intended for public-facing production deployment as part of this course. It is a reproducible research artifact, not a SaaS product.

**Reproducibility target.** A graduate-level reader on a stock Ubuntu 22.04 or 24.04 host with Docker pre-installed should be able to:

```
git clone <repo>
cd safeexec
make setup        # installs gVisor, builds Docker images, pulls test corpora
make test         # runs functional + adversarial suite under both back-ends
make bench        # runs the benchmark sweep, emits a result table
```

…and obtain reported numbers within ±10% on equivalent hardware.

**Deliverable submission package.**
- GitHub repository link (visibility decided in §6 below).
- Final PDF technical report.
- Presentation slide deck.
- Pre-recorded demo screencast as backup (in case live demo fails in the defense session).

**Reproducibility risks.**
- Reader on ARM Mac with Docker Desktop instead of native Linux: gVisor support on macOS is unofficial; project will document "tested on x86-64 Ubuntu" and accept this limitation.
- Reader without root on their evaluation host: gVisor installation requires apt-add-repository; document this as a precondition in the README.
- Reader without an Anthropic API key: the reference-agent demo will refuse to run, but every other test target is API-independent.

Decide repository visibility: **Public from the start** (slightly stronger portfolio signal but cannot be undone).

## 5. Time constraints

The charter's milestone map is the time budget. Critical timing risks:

**W5 hard checkpoint.** "Hello world Python execution under hardened Docker, returning structured JSON output." If missed by end of W5, the W7 midpoint review will trigger the scope-reduction fallback (Docker-only back-end, gVisor demoted to stretch). This is named in the charter risk register.

**W7 midpoint review.** Functional suite ≥100, adversarial taxonomy locked, ≥20 adversarial programs working. This is the explicit re-scoping point per the charter.

**W11 draft due.** Full technical report draft to supervisor. This is the deadline that should *most* be calendar-blocked now — supervisor feedback turnaround drives W12 revision quality.

**W13 hard freeze.** Presentation deck + demo script + AI-use appendix consolidated. No new feature work past this date.

Wall-clock effort estimate (student hours):
- W1–W2 launch packet: ~25 hours (much of W1 already invested).
- W3–W4 design + lit synthesis: ~30 hours.
- W5–W6 hardened-Docker implementation: ~40 hours.
- W7 midpoint demo prep: ~15 hours.
- W8 gVisor implementation: ~25 hours.
- W9–W10 results, hardening, reproducibility: ~30 hours.
- W11 full draft: ~30 hours.
- W12 revisions: ~20 hours.
- W13 rehearsal + AI-use appendix: ~10 hours.
- W14 final submission + reflection: ~10 hours.

**Total: ~235 hours.** Across 14 weeks that is ~17 hours/week — consistent with a 3-credit graduate applied-project workload. If the student's actual availability is materially below this, the W7 scope-reduction trigger is the relief valve, not a quality compromise.

Confirmed realistic weekly availability with supervisor. 

## 6. Personnel / external dependencies

Sole-student project. External dependencies are limited to supervisor availability:

| Dependency | Required by | Mitigation if delayed |
|---|---|---|
| Supervisor charter approval | W2 (2026-05-22) | Begin W3 lit-synthesis on the *assumption* of approval; revise scope if approval comes back with material changes. |
| Supervisor midpoint feedback | W7 (2026-06-26) | If feedback delayed >1 week, default to executing the gVisor sprint per plan and adjusting at next supervisor meeting. |
| Supervisor draft feedback | W11 (2026-07-24) | Submit draft early in W11 to leave buffer for slow turnaround. |

Confirm supervisor availability windows for W2, W7, W11 before W1 submission. Propose a standing fortnightly check-in cadence at the W2 meeting.

## 7. Summary feasibility judgment

The project is feasible within the stated constraints:
- **Data:** no external dataset dependency; functional corpus has permissively-licensed candidates; adversarial corpus is authored work.
- **Compute:** ~$150–$250 expected budget, well inside the charter's ~$200–$400 envelope; primary compute is a small Linux VM that any of three providers can supply.
- **Software:** all dependencies are open-source and have well-documented Ubuntu install paths; no exotic kernel patches or research-only tooling.
- **Deployment:** reproducibility target is achievable with stock tooling; risks (ARM hosts, gVisor install permission) documented and accepted.
- **Time:** ~235 student-hours across 14 weeks (~17 hrs/wk); two explicit relief valves (W5 checkpoint, W7 scope review) handle slippage.
- **Personnel:** only external dependency is supervisor availability for three named milestones.

The six student decisions named above are all resolved.

**Recommendation:** proceed to W2 charter approval.

---

## Six student decisions, summarized for the supervisor meeting

| # | Decision | |
|---|---|--|
| D1 | Redistribute HumanEval/MBPP subset |
| D2 | Compute provider — DigitalOcean / HU lab | |
| D3 | Ubuntu 22.04 host? | |
| D4 | Repository visibility — public | |
| D5 | Weekly availability — ≥12 hrs/week confirmed | |
| D6 | Supervisor cadence — fortnightly check-ins + the three named milestones? | |
