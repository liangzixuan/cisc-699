# AI-Use Disclosure Log

This document tracks every substantive use of generative AI in this project. It is the source from which the final report's AI-use appendix will be assembled. Per the CISC 699 syllabus, AI-generated text, code, analysis, or figures may not be submitted as unaided work, and all substantial AI assistance must be disclosed.

Conventions:
- One entry per AI-assisted session (or per artifact, when assistance spans a session).
- Record: date, tool/model, artifact affected, what was generated vs. what the student authored or revised, and a brief note on verification (did the student check correctness, edit substantively, validate against sources?).
- Confidential, proprietary, FERPA, or HIPAA-regulated data is **not** to be entered into public AI systems.

---

## W1 — Project initialization (2026-05-13)

**Tool / model:** Claude (Anthropic) — Cowork desktop app, Sonnet 4.6.

**Artifacts touched:**

| File | AI contribution | Student contribution required before submission |
|---|---|---|
| `README.md` | Initial draft of project framing, repo layout summary, status table, evaluation paragraph. | Review, edit into own voice, confirm milestone dates against syllabus, replace working title if changed. |
| `engineering-log.md` | Initial structure, W1 seed entries. | Take over weekly authorship; entries from W2 onward are student-written. |
| `.gitignore` | Standard Python/IDE/Docker ignore patterns. | Sanity-check, add project-specific patterns as repo grows. Low-judgment content. |
| `docs/01-launch-packet/problem-statement.md` | One-paragraph problem statement framing the LLM-agent sandbox motivation. | Substantively revise into own voice; verify each empirical claim (e.g., "closed-source services such as ... address these risks behind opaque infrastructure") against cited sources before submission. |
| `docs/01-launch-packet/candidate-projects.md` | Comparison of three candidate projects (agent eval harness, multi-model router, hardened sandbox); selection rationale. | Verify the comparison reflects the student's actual reasoning; rewrite selection rationale in own voice. |
| `docs/01-launch-packet/project-charter.md` | Full charter draft: rationale, intended artifact, users, goals, scope (in/out), assumptions, stakeholders, risks, success criteria, milestone map, approval block. | Substantively revise. Confirm all dates, budget assumptions, and risk mitigations. The charter must reflect the student's commitments, not Claude's recommendations, before being submitted for approval. |
| `docs/01-launch-packet/feasibility-memo.md` (stub) | Section outline only. | Author all substance. |
| `docs/01-launch-packet/annotated-bibliography.md` | (See dedicated W1 bibliography entry below — superseded.) | (See below.) |
| `docs/01-launch-packet/supervisor-briefing.md` (stub) | Section outline. | Author content based on student's own questions for the supervisor. |

**Conversational AI assistance (not written into any artifact, but shaped the project's direction):**
- Brainstorm of three candidate projects and tradeoffs.
- Identification of project risks (scope creep, evaluation-framing difficulty).
- Recommendation of two-back-end design (hardened Docker + gVisor) with an adversarial test suite as the unique contribution.
- Suggested seven W1 deliverables in workflow order.

**Verification status (as of 2026-05-17):**
- All source citations have been independently verified — student completed literature review.
- No code has been written or executed yet.
- Empirical claims in the problem statement has been verified by student.

**Sensitive data:** None entered into the AI system. The course context (CLAUDE.md), the project launch packet PDF, and the syllabus are non-confidential course materials.

---

---

## W1 — Annotated bibliography draft (2026-05-13)

**Tool / model:** Claude (Anthropic) — Cowork desktop app, Sonnet 4.6, with `WebSearch` and `web_fetch` tools.

**Artifact touched:** `docs/01-launch-packet/annotated-bibliography.md` (replaced earlier stub with a 7-entry IEEE-formatted draft).

**Workflow used.** The assistant ran web searches for candidate sources across the five bibliography categories from the original stub, then fetched the most credible-looking primary source for each via `web_fetch` and drafted annotations grounded *only* in content actually retrieved. Each annotation ends with a "Verification status" line recording exactly what the assistant verified and what the student still must verify before submission.

**Searches run (queries logged for reproducibility):**
- "NIST AI 100-2 adversarial machine learning taxonomy 2025"
- "OWASP Top 10 LLM applications 2025 code execution sandbox"
- "gVisor application kernel containers Young Lacasse 2018 design paper"
- "Firecracker lightweight virtualization serverless NSDI 2020 Agache"
- "SWE-bench Jimenez evaluating language models software engineering ICLR 2024"
- "runc CVE-2019-5736 container escape vulnerability technical analysis"
- "E2B sandbox AI agent code execution architecture documentation"
- "Greg Brockman seccomp BPF Linux kernel syscall filtering" (used to surface kernel.org primary docs; entry deferred)

**URLs fetched in full:**
- https://csrc.nist.gov/pubs/ai/100/2/e2025/final (NIST publication record — abstract, authors, DOI verified)
- https://genai.owasp.org/llm-top-10/ (OWASP LLM Top 10 2025 landing page — categories LLM01–LLM10 verified)
- https://github.com/SWE-bench/SWE-bench (SWE-bench README — BibTeX citation verified)
- https://access.redhat.com/security/vulnerabilities/runcescape (Red Hat CVE-2019-5736 advisory — attack mechanism and mitigations verified)
- https://gvisor.dev/docs/ (gVisor "What is gVisor?" page — Sentry/Gofer architecture verified)
- https://github.com/e2b-dev/E2B (E2B repository README — license, scope, SDKs verified)

**URLs attempted but not retrieved (rate-limit or empty response):**
- https://www.usenix.org/conference/nsdi20/presentation/agache (Firecracker abstract page; cross-referenced via search-result content instead)
- https://www.usenix.org/system/files/hotcloud19-paper-young.pdf (gVisor case study paper — deferred to W11 expansion)
- https://arxiv.org/abs/2310.06770 (SWE-bench arXiv abstract — cross-referenced via project README instead)

**Entries drafted (7):** [1] NIST AI 100-2 E2025 (A); [2] OWASP LLM Top 10 2025 (A); [3] gVisor documentation (B); [4] Firecracker NSDI 2020 paper (B); [5] E2B repository (C); [6] SWE-bench ICLR 2024 (D); [7] CVE-2019-5736 Red Hat advisory (E).

**Specific verification gaps recorded in the bibliography file itself. (Completed)** Each entry's "Verification status" line names what was *not* retrieved by the assistant. The student must close each of these gaps before submission (Completed). The most important gaps to close are: (a) reading the actual OWASP LLM05 / LLM06 detail pages (not just the landing page); (b) reading the Firecracker NSDI paper PDF rather than relying on the search-result summary; (c) reading the gVisor security model and performance pages to confirm the performance-tradeoff claim made in the annotation. (Completed)

**Sensitive data:** None entered into the AI system. All sources are public web pages.

**What was *not* done by the AI.** The AI did not fabricate any citation. The AI did not provide annotations for any source whose page it failed to retrieve. The AI did not summarize papers from training-data knowledge alone — every annotation is grounded in fetched content, and where the assistant's training-data knowledge was used at all (e.g., for the Firecracker entry, which relied on search-result summaries rather than the paper PDF), the verification-status line records that explicitly.

---

---

## W1 — Remaining launch-packet artifacts (2026-05-14)

**Tool / model:** Claude (Anthropic) — Cowork desktop app, Sonnet 4.6, with `WebSearch`, `web_fetch`, and `mcp__workspace__bash` tools.

**Artifacts touched.** Drafted the remaining deliverables required by the launch packet's "Suggested submission package" and the "Tools (Architectures)" evidence requirement:

| File | AI contribution | Student contribution required before submission |
|---|---|---|
| `docs/01-launch-packet/architecture-context.md` | Mermaid system-context diagram + scope-boundary explanation; commitment notes for what the diagram pins down. | Export to static SVG/PNG via mermaid.live for Canvas attachment. Confirm the boundary lines match the charter — they should — and adjust either one if not. Revise prose into own voice. |
| `docs/01-launch-packet/feasibility-memo.md` | Replaced earlier outline stub with substantive content: licensed-corpus options (HumanEval, MBPP), three cloud-host options with ballpark pricing, software dependency matrix, deployment expectations, time budget (~235 student hours total). Six `STUDENT DECISION` markers (D1–D6) flagging items that require student/supervisor input. | Resolve D1–D6 personally and/or at the W2 supervisor meeting. Verify all pricing at signup (ballparks were assistant-supplied based on publicly listed rates and are subject to change). |
| `docs/01-launch-packet/w2-github-issues.md` | Pre-drafted 17 GitHub issues (W1 closeout, W2, W3, W4, W5 kickoff) with titles, labels, and bodies; intended for copy-paste into a GitHub issue tracker. | Push these into the actual issue tracker once the GitHub remote exists (see `git-push-instructions.md`). |
| `docs/01-launch-packet/screenshots-checklist.md` | List of 5 required + 2 optional screenshots with capture commands and rationale per requirement. | Capture the screenshots. Cannot be AI-generated. |
| `docs/01-launch-packet/git-push-instructions.md` | Two procedures (`gh` CLI and web-UI) for creating a private GitHub remote and pushing the W1 commit. | Run one of them. Cannot be AI-executed — needs GitHub credentials. |
| `.gitattributes` | Standard line-ending and binary-file rules + linguist-generated markers. | Sanity-check; low-judgment content. |

**Tools used.** `mcp__workspace__bash` for `git init`, branch configuration, `git add`, `git commit`, and `git tag` operations. The initial commit (hash `2a280e6`, tag `w1-initial`) was made by Claude on behalf of the student. Author/committer is configured to "Eric Liang <cary.wheatman@gmail.com>" per the user identity provided to Cowork.

**Verification Completed.**
- Student decided on using GitHub education pack DigitalOcean free credits.
- The Mermaid diagram was rendered to a static image in this session.

**Sensitive data:** None entered into the AI system.

---

## Going forward — what to log

Add a new entry below for any of the following:

- AI assistance with drafting the final report or any of its sections
- AI-generated code that is committed to the repository (with a pointer to the commit)
- AI-assisted debugging that led to a non-obvious fix (commit pointer + brief explanation)
- AI-assisted literature search or summarization (always verify the source exists and read it before citing)
- AI-generated figures, tables, or analysis
- AI assistance with the adversarial test suite design (this is the project's central contribution and warrants particular care — student-authored programs preferred, AI assistance disclosed)

Conversely, items that do **not** require an entry: minor IDE autocomplete, grammar/spell-check, brainstorming that did not result in committed content.
