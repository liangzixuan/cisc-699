# Advisor Briefing Note — Week 1

> **AI-use disclosure.** Drafted with Claude Sonnet 4.6 (Cowork desktop app). AI-drafted, student-revised. Key human-authored decisions in this document: choice of advisor questions; recipient list (Prof. Khalid Lateef as project advisor and Dr. Majid Shaalan as course instructor); §5 revision to reflect actual W2 commitments (the original AI draft contained stale W2 items already completed in W1). Full audit trail: [`docs/ai-use-log.md`](../ai-use-log.md).

**To:** Prof. Khalid Lateef
**CC:** Dr. Majid Shaalan
**From:** Zixuan Liang
**Subject:** CISC 699 Summer 2026 — proposed applied project (SafeExec: hardened Python execution sandbox for LLM agents)
**Date:** *(populate before sending)*

## 1. One-paragraph summary

I am proposing a hardened, threat-modeled Python execution sandbox designed for use as a tool by LLM-powered software agents (agents in the lineage of Claude Code, Code Interpreter, and similar systems). The artifact is a small HTTP service that accepts Python code and runs it inside an isolated environment, with two pluggable isolation back-ends (a hardened Docker configuration and a gVisor-backed configuration). The intellectual contribution is a curated adversarial test suite — roughly 40 programs across categories like resource exhaustion, fork bombs, syscall abuse, and attempted exfiltration — and an empirical comparison of isolation strength and performance overhead across the two back-ends. The full charter draft and a three-candidate comparison are in `docs/01-launch-packet/`.

## 2. Why this project for me

This project sits at the intersection of (a) production software engineering, (b) systems and Linux security primitives, and (c) the agentic-LLM domain that is currently a major area of industry hiring — which aligns with my career objective of moving toward software-engineering roles at frontier AI labs. The project does not require model training, novel ML methodology, or specialized hardware, which means I can focus my 14 weeks on doing the systems and evaluation work *well* rather than learning ML internals from scratch alongside it.

## 3. What I'm asking from you in W2

The launch packet asks me to "list the decisions still needed from a Week 1 conversation." Mine are below, ordered roughly by impact.

### Decisions

1. **Project approval at the proposed scope.** Is the Python-only, two-back-end, ≥40-program adversarial suite the right size for CISC 699? I have a fallback plan (Candidate A in `candidate-projects.md`) if you'd prefer a less systems-heavy artifact.
2. **Framing of the "contribution."** I am positioning the adversarial test suite and its evaluation methodology as the project's intellectual contribution, rather than positioning a novel isolation technique as the contribution. Is that framing acceptable to you?
3. **Open-source release.** Are you comfortable with me releasing the artifact (code + adversarial suite) under an open-source license at the end of the term, or would you prefer it remain private?
4. **Reference-agent demo.** I plan to build a small Claude-API-driven agent (≤50 lines) that uses the sandbox as a tool, included strictly as integration demo. Is that scope acceptable, or would you prefer no third-party API in the demo path?

### Clarifications / preferences

5. **Repository / version-control arrangement.** Is a private GitHub repo with a final share link to the advisor acceptable, or does the program have a preferred host (HU GitLab, etc.)?
6. **Report and presentation templates.** Are there CISC 699 templates (Word, LaTeX, Beamer) you expect me to use, or am I free to choose?
7. **Citation style.** IEEE, ACM, APA — any preference?
8. **Meeting cadence.** How often would you like to meet? My default proposal: standing 30-minute check-in every two weeks, plus dedicated longer sessions at W2 (charter approval), W4 (design review), W7 (midpoint), W11 (draft feedback).

### Risks I'd like your read on

9. **Adversarial-suite quality risk.** The suite's quality is the project's central evaluation contribution. I'd like your input on what constitutes "credible" — categories, sample size per category, the right balance between hand-authored and CVE-derived programs.
10. **gVisor variability risk.** gVisor performance is reportedly variable; my evaluation plan addresses this with sample-size analysis and percentile-based reporting. I'd like your sanity-check on the proposed protocol before W4 design review.

## 4. What I have done already in W1

- Drafted the project charter, problem statement, three-candidate comparison, feasibility memo, and advisor briefing (this document).
- Set up the project repository at `https://github.com/liangzixuan/cisc-699` with the structure described in `README.md`.
- Started the engineering log (`engineering-log.md`) and AI-use disclosure log (`docs/ai-use-log.md`).
- Identified five source categories for the annotated bibliography and the gaps I still need to fill (`https://github.com/liangzixuan/cisc-699/blob/main/docs/01-launch-packet/annotated-bibliography.md`).

## 5. What I plan to do in W2

- incorporate advisor feedback into the charter
- expand the bibliography toward the W11 ≥15-source target
- start W3 lit-synthesis and requirements work

## 6. Attachments

- `https://github.com/liangzixuan/cisc-699/blob/main/docs/01-launch-packet/project-charter.md`
- `https://github.com/liangzixuan/cisc-699/blob/main/docs/01-launch-packet/problem-statement.md`
- `https://github.com/liangzixuan/cisc-699/blob/main/docs/01-launch-packet/candidate-projects.md`
- `https://github.com/liangzixuan/cisc-699/blob/main/docs/01-launch-packet/feasibility-memo.md`
- `https://github.com/liangzixuan/cisc-699/blob/main/docs/01-launch-packet/annotated-bibliography.md` (in-progress)

---
