# One-Page Approval Brief — SafeExec (W2 Proposal Approval Package, Appendix A)

> **AI-use disclosure.** Drafted with Claude Sonnet 4.6 (Cowork desktop app). AI-drafted, student-revised. Key human-authored decisions in this document: the choice of which items belong in "Approved," "Conditional," and "Evidence expected by W4" — these are commitments to the advisor and were assigned by the student. Full audit trail: [`docs/ai-use-log.md`](../ai-use-log.md).

**Project:** SafeExec — A hardened, threat-modeled Python execution sandbox for LLM-agent tool-use.
**Student:** Zixuan Liang.
**Project advisor:** Prof. Khalid Lateef.
**Course instructor:** Dr. Majid Shaalan.
**Course:** CISC 699-50-A-2026/Summer.
**Term:** 2026-05-09 → 2026-08-14.
**Brief date:** 2026-05-21.
**Status:** Approved / strong Level 1 feedback received 2026-05-28. Main follow-up: prioritize execution discipline, benchmark definition, and implementation-risk control over additional documentation growth.

---

## What was approved

- **Scope.** Python-only execution; two isolation back-ends (hardened Docker + gVisor); single-tenant; no network; no GPU; Linux x86-64 host (Ubuntu 22.04 LTS). The full in/out-of-scope list is `proposal.md` §8.
- **Central contribution.** Adversarial test suite of ≥40 programs across ≥6 categories with documented expected-contained-outcome labels, paired with an empirical isolation-vs-overhead comparison across the two back-ends.
- **Success criteria (measurable).** Functional ≥99%; isolation ≥90% Docker / ≥95% gVisor; ≥30 samples per benchmark condition with 95% CI; reproducibility within ±10% on equivalent hardware. Full table in `proposal.md` §7.
- **Project plan.** 14-week plan with six explicit completion gates (G1 W2 proposal approval, G2 W4 design review, G3 W5 first execution, G4 W7 midpoint demo, G5 W11 full draft, G6 W14 final submission). Critical-path chain and contingency dates in `project-plan.md`.
- **Risk register.** 12 risks with likelihood / impact / mitigation / owner / contingency. Two relief valves named explicitly: W5 hello-world checkpoint, W7 midpoint scope renegotiation.
- **AI-use disclosure.** Audit-table format adopted 2026-05-18 in response to W1 grading feedback; inline disclosure block on every substantive artifact; W14 appendix will be consolidated from `docs/ai-use-log.md`.
- **Reproducibility commitment.** `make setup && make test && make bench` on stock Ubuntu 22.04/24.04; numbers within ±10% on equivalent hardware; pre-rendered result tables and a pre-recorded demo as fallbacks.

## What remains conditional after approval feedback

The W2 feedback identified no conceptual blocker. The remaining conditional items are execution-control items to carry into W4-W7:

1. **Implementation burden.** gVisor integration, hardened runtime behavior, and adversarial benchmarking are substantial for one student. Keep both backends in plan, but preserve W7 fallback and front-load runnable code.
2. **Benchmark definition.** W4 must operationalize containment labels, pass/fail rules, sample counts, overhead metrics, and reporting format before implementation expands.
3. **Scope discipline.** Keep Python-only, no network, no GPU, single-tenant, and no persistence. Treat additional features as out of scope unless they directly reduce implementation risk.
4. **Walkthrough delivery.** Written materials are strong; graded walkthrough/presentation quality still depends on concise delivery and rehearsal against timing.

Any follow-up change is tracked in `engineering-log.md`; no concept-level rescope is required by the W2 feedback.

## Evidence expected by the next checkpoint (W4 design review, 2026-06-05)

Between this approval feedback (received 2026-05-28) and the W4 design review, the following artifacts will be produced:

- `docs/design/requirements.md` v1.0 — functional and non-functional requirements with traceability to the success criteria in `proposal.md` §7.
- `docs/design/architecture.md` — component-level design beyond the W1 system-context view: API request lifecycle, executor-interface contract, back-end-specific component layouts, cgroup hierarchy, seccomp filter scope.
- `docs/design/threat-model.md` — named adversary capabilities, named defenses, mapping to OWASP LLM05/LLM06 and to NIST AI 100-2 categories. Adversarial-suite category taxonomy locked at the *category* level (per-program lock is W7).
- `docs/design/evaluation-plan.md` — benchmark protocol (warm-up runs, sample size, percentile reporting, CI method); functional-corpus composition with redistribution-licensing checks; adversarial-suite category counts with rationale.
- Annotated bibliography expanded to ≥10 entries (current 7), with category balance (≥1 prompt-injection source, ≥1 seccomp primary source, ≥1 academic gVisor performance source).
- Engineering-log entries for W3 and W4 documenting decisions, blockers, and any scope notes.

The advisor's W4 design-review approval (G2) is the gate that allows Phase III implementation to begin. The W2 feedback changes the emphasis: the W4 package should define implementation and benchmark details clearly, then stop expanding documentation and move toward runnable code.

## What success looks like at this hard stop

The W2 deliverable is graded on (per rubric RU-02):

- Problem Statement and Success Criteria (10 pts) — `proposal.md` §§3, 4, 7.
- Proposal Quality and Project Plan (10 pts) — `proposal.md` §§1–18 and `project-plan.md`, `wbs.md`.
- Technical Feasibility and MACP Framing (10 pts) — `proposal.md` §9.
- Risk, Ethics, and Constraints Management (10 pts) — `proposal.md` §§12–14.
- AI Usage Log and Academic Integrity (10 pts) — `docs/ai-use-log.md`, plus the inline block at the top of every W2 artifact.
- Recorded Walkthrough of Problem Framing and Project Development (50 pts) — `walkthrough-script.md` and the recorded video file.

Total: 100 pts. Target: Level 1 (Advanced/Exceptional, 90–100%) on every dimension.

---

*Signed:*

| Role | Name | Decision | Date |
|---|---|---|---|
| Student | Zixuan Liang | Submitted | 2026-05-23 |
| Project advisor | Prof. Khalid Lateef | Approved / strong Level 1 feedback | 2026-05-28 |
| Course instructor | Dr. Majid Shaalan | _not required for scope sign-off_ | ___________________ |

*End of approval brief.*
