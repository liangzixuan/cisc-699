# Work Breakdown Structure (WBS) — SafeExec (W2 Proposal Approval Package, Appendix B)

> **AI-use disclosure.** Drafted with Claude Sonnet 4.6 (Cowork desktop app). AI-drafted, student-revised. Key human-authored decisions in this document: every task estimate; every traceability map from WBS task to success criterion; every "blocked by" link; the choice to keep estimates as ranges rather than point values. Full audit trail: [`docs/ai-use-log.md`](../ai-use-log.md).

This document is the WBS appendix for the W2 Proposal Approval Package. Every leaf task is mapped to (a) the week it is scheduled, (b) the deliverable it produces, (c) the success criterion in `proposal.md` §7 it advances, and (d) any blocking dependency. The instructor's self-check — *"can every task in your plan be traced to a success criterion?"* — is satisfied by the SC column.

## Legend

- **ID:** stable identifier; cited from `proposal.md` §11 and from `engineering-log.md`.
- **Est:** student-hours estimate as a range; total at the bottom.
- **SC:** success criterion in `proposal.md` §7 this task advances. Sub-criteria (7.1 functional, 7.2 isolation, 7.3 performance, 7.4 reproducibility, 7.5 communication, 7.6 process).
- **Blocks:** WBS IDs that cannot start until this one completes.
- **Status:** `done | in-progress | pending`.

---

## Phase I — Launch (W1–W2)

| ID | Task | Week | Est (hrs) | Deliverable | SC | Blocks | Status |
|---|---|---|---|---|---|---|---|
| WBS-1.1 | Submit W1 launch packet | W1 | 25 | Canvas submission (graded 90/100) | 7.6 | WBS-1.2 | done |
| WBS-1.2 | Strengthen AI-use log (post-feedback) | W2 | 4 | Audit-table format in `docs/ai-use-log.md` | 7.6 | — | done |
| WBS-1.3 | Draft W2 proposal-approval package | W2 | 12 | This document set | 7.5, 7.6 | WBS-1.4, WBS-2.1 | in-progress |
| WBS-1.4 | Record walkthrough video (≤15 min) | W2 | 4 | `walkthrough-script.md` + recorded `.mp4` | 7.5 | — | pending |
| WBS-1.5 | Submit W2 proposal package to Canvas | W2 | 1 | Canvas submission | 7.6 | WBS-1.3, WBS-1.4 | pending |

Phase I subtotal: **~46 hours**. Actual W1 spend was front-loaded; W2 spend is ~21 hours over a 7-day window.

---

## Phase II — Design (W3–W4)

| ID | Task | Week | Est (hrs) | Deliverable | SC | Blocks | Status |
|---|---|---|---|---|---|---|---|
| WBS-2.1 | Lit synthesis: expand bibliography to ≥10 entries | W3 | 6 | `annotated-bibliography.md` updated | 7.6 | WBS-2.2 | pending |
| WBS-2.2 | Requirements & use cases | W3 | 8 | `docs/design/requirements.md` v1.0 | 7.5 | WBS-2.3 | pending |
| WBS-2.3 | Architecture detailed design | W4 | 10 | `docs/design/architecture.md` | 7.1 | WBS-3.1, WBS-3.2 | pending |
| WBS-2.4 | Threat model | W4 | 8 | `docs/design/threat-model.md` | 7.2 | WBS-3.6, WBS-3.8 | pending |
| WBS-2.5 | Evaluation plan | W4 | 6 | `docs/design/evaluation-plan.md` | 7.1–7.4 | WBS-3.12 | pending |

Phase II subtotal: **~38 hours** across W3–W4.

---

## Phase III — Implementation (W5–W8)

### Sprint I (W5) — Docker baseline + first execution

| ID | Task | Week | Est (hrs) | Deliverable | SC | Blocks | Status |
|---|---|---|---|---|---|---|---|
| WBS-3.1 | Execution API skeleton | W5 | 8 | `src/api/` first commit; `/execute` returns request echo | 7.1 | WBS-3.2 | pending |
| WBS-3.2 | Docker baseline back-end | W5 | 10 | First end-to-end Python execution (G3 gate) | 7.1 | WBS-3.4 | pending |
| WBS-3.3 | Functional corpus seed (≥30 programs) | W5 | 6 | `tests/functional/` seeded from HumanEval | 7.1 | WBS-3.5 | pending |

Sprint I subtotal: **~24 hours**.

### Sprint II (W6) — Hardened Docker + corpus growth

| ID | Task | Week | Est (hrs) | Deliverable | SC | Blocks | Status |
|---|---|---|---|---|---|---|---|
| WBS-3.4 | Harden Docker back-end (seccomp + AppArmor + cgroups + read-only rootfs) | W6 | 14 | Hardened back-end commits | 7.2 | WBS-3.10 | pending |
| WBS-3.5 | Functional corpus to ≥50 programs | W6 | 4 | `tests/functional/` | 7.1 | WBS-3.7 | pending |
| WBS-3.6 | Adversarial corpus seed (≥10 programs, ≥3 categories) | W6 | 6 | `tests/adversarial/` | 7.2 | WBS-3.8 | pending |

Sprint II subtotal: **~24 hours**.

### Midpoint week (W7) — taxonomy lock + scope renegotiation

| ID | Task | Week | Est (hrs) | Deliverable | SC | Blocks | Status |
|---|---|---|---|---|---|---|---|
| WBS-3.7 | Functional corpus to ≥100 programs | W7 | 4 | `tests/functional/` | 7.1 | — | pending |
| WBS-3.8 | Adversarial taxonomy locked; ≥20 programs running | W7 | 6 | `tests/adversarial/README.md`; threat-model update | 7.2 | WBS-3.11 | pending |
| WBS-3.9 | Midpoint demo + scope renegotiation (G4 gate) | W7 | 4 | Demo recording; supervisor decision log entry | 7.5 | WBS-3.10 | pending |

Midpoint subtotal: **~14 hours** (intentionally light — week is buffer + checkpoint).

### Sprint III (W8) — gVisor + adversarial completion + performance harness

| ID | Task | Week | Est (hrs) | Deliverable | SC | Blocks | Status |
|---|---|---|---|---|---|---|---|
| WBS-3.10 | gVisor back-end integration | W8 | 12 | gVisor commits; both back-ends executable | 7.2 | WBS-3.12 | pending |
| WBS-3.11 | Adversarial corpus to ≥40 programs across ≥6 categories | W8 | 8 | `tests/adversarial/` | 7.2 | WBS-4.1 | pending |
| WBS-3.12 | Performance benchmark harness + first sweep | W8 | 6 | `benchmarks/results/` initial results | 7.3 | WBS-4.1 | pending |

Sprint III subtotal: **~26 hours**.

Phase III subtotal: **~88 hours** (W5–W8 combined).

---

## Phase IV — Results & hardening (W9–W10)

| ID | Task | Week | Est (hrs) | Deliverable | SC | Blocks | Status |
|---|---|---|---|---|---|---|---|
| WBS-4.1 | Full performance sweep on both back-ends | W9 | 6 | `benchmarks/results/` tables, plots | 7.3 | WBS-4.2 | pending |
| WBS-4.2 | Results, limitations, broader-impact draft | W9 | 12 | Report §§7–9 drafted | 7.5 | WBS-5.1 | pending |
| WBS-4.3 | Reproducibility materials (README, Makefile, setup.sh) | W10 | 10 | `deploy/setup.sh`, `Makefile`, README update | 7.4 | WBS-4.4 | pending |
| WBS-4.4 | Clean-VM reproducibility self-test (fresh droplet) | W10 | 6 | Fresh-droplet results within ±10% | 7.4 | WBS-5.1 | pending |

Phase IV subtotal: **~34 hours**.

---

## Phase V — Reporting (W11–W12)

| ID | Task | Week | Est (hrs) | Deliverable | SC | Blocks | Status |
|---|---|---|---|---|---|---|---|
| WBS-5.1 | Full report draft to supervisor (G5 gate) | W11 | 22 | `docs/reports/final-report.md` v0.9 | 7.5 | WBS-5.3 | pending |
| WBS-5.2 | Bibliography to ≥15 sources | W11 | 8 | `annotated-bibliography.md` updated | 7.6 | WBS-5.1 | pending |
| WBS-5.3 | Revision cycle on advisor feedback | W12 | 14 | Final report v1.0 | 7.5 | WBS-6.1 | pending |
| WBS-5.4 | Slide deck + demo script | W12 | 6 | `docs/reports/slides.pptx` v0.9; `scripts/demo_script.md` | 7.5 | WBS-6.1 | pending |

Phase V subtotal: **~50 hours**.

---

## Phase VI — Defense (W13–W14)

| ID | Task | Week | Est (hrs) | Deliverable | SC | Blocks | Status |
|---|---|---|---|---|---|---|---|
| WBS-6.1 | Presentation rehearsal | W13 | 4 | Rehearsal recording ≤20 min | 7.5 | WBS-6.3 | pending |
| WBS-6.2 | AI-use appendix consolidated | W13 | 4 | Report appendix from `docs/ai-use-log.md` | 7.6 | WBS-6.3 | pending |
| WBS-6.3 | Final submission package (G6 gate) | W14 | 6 | Canvas final upload: report PDF, repo link, slides, demo recording | 7.5, 7.6 | — | pending |
| WBS-6.4 | Reflection / lessons learned | W14 | 2 | `docs/reports/reflection.md` | 7.6 | — | pending |

Phase VI subtotal: **~16 hours**.

---

## Totals

| Phase | Estimated hours | % of total |
|---|---|---|
| Phase I — Launch | 46 | 19% |
| Phase II — Design | 38 | 16% |
| Phase III — Implementation | 88 | 36% |
| Phase IV — Results & hardening | 34 | 14% |
| Phase V — Reporting | 50 | 21% |
| Phase VI — Defense | 16 | 7% |
| **Total** | **~272 hrs** | (range: ~235–290) |

The W1 feasibility memo's estimate was ~235 hours; this WBS lands at ~272 with the contingency buffer included. Both numbers are consistent with ~17–20 hours/week across 14 weeks. If the realized number drops materially, the W7 scope-reduction trigger is the relief valve.

## Traceability — every success criterion has at least one task

| Success criterion | Covered by WBS tasks |
|---|---|
| 7.1 Functional correctness | WBS-2.3, WBS-3.1, WBS-3.2, WBS-3.3, WBS-3.5, WBS-3.7 |
| 7.2 Isolation strength | WBS-2.4, WBS-3.4, WBS-3.6, WBS-3.8, WBS-3.10, WBS-3.11 |
| 7.3 Performance | WBS-2.5, WBS-3.12, WBS-4.1 |
| 7.4 Reproducibility | WBS-4.3, WBS-4.4 |
| 7.5 Communication | WBS-1.3, WBS-1.4, WBS-2.2, WBS-3.9, WBS-4.2, WBS-5.1, WBS-5.3, WBS-5.4, WBS-6.1, WBS-6.3 |
| 7.6 Process | WBS-1.1, WBS-1.2, WBS-1.5, WBS-2.1, WBS-5.2, WBS-6.2, WBS-6.4 |

Every WBS task maps to ≥1 success criterion; every success criterion is covered by ≥2 WBS tasks. Instructor self-check satisfied.

---

*End of WBS.*
