# Recorded Walkthrough Script — SafeExec Proposal (W2 Hard Stop 1, Appendix D)

> **AI-use disclosure.** Drafted with Claude Sonnet 4.6 (Cowork desktop app). AI-drafted, student-revised. Key human-authored decisions in this document: every minute-budget allocation (the timing reflects the student's own pacing rehearsal, not the AI's first guess); the choice to make Decision Authorship a named segment rather than burying it in a closing note; the explicit ownership-of-trade-offs language in segments 5 and 7. Full audit trail: [`docs/ai-use-log.md`](../ai-use-log.md).

## Purpose

This is the script for the **recorded walkthrough** required by the W2 rubric (RU-02 dimension 6: *"Recorded Walkthrough of Problem Framing and Project Development"* — 50 of 100 points). The rubric asks for a clear, well-organized walkthrough of the problem framing, charter, scope, feasibility logic, and planned development path; it asks the student to explain key decisions, trade-offs, and next steps with confidence and strong technical ownership.

## Production notes

- **Target length:** 14:30–15:30. Hard ceiling 16:00 — beyond that the recording risks signaling weak editing rather than strong substance.
- **Format:** Screen recording (1920×1080) with picture-in-picture webcam (top right, ~20% of frame). Camera is optional but recommended — the rubric language about "technical ownership" rewards a visible human.
- **Tools:** OBS Studio for capture; QuickTime or ScreenStudio acceptable. Microphone: any headset mic; record in a quiet room.
- **Filename:** `safeexec-w2-walkthrough.mp4` (≤500 MB target; H.264, 8 Mbps, AAC audio).
- **Upload destination:** Canvas (media recording field) or YouTube unlisted with link in Canvas text entry. Confirm with course rules before recording.
- **Audio check:** Read the first 30 seconds aloud and play it back before recording the full take. The most common reason this kind of recording fails the rubric is unintelligible audio in segment 1.
- **One take vs. multi-take:** One take is acceptable; jump cuts at section boundaries are fine. Do not over-edit — the rubric rewards natural ownership over polish.

## Materials on screen during the walkthrough

The "show on screen" cues below reference these source files. Have them open as tabs in the browser or panes in the IDE before recording starts.

1. `README.md` — opening tab
2. `docs/02-proposal-package/proposal.md` — primary reference
3. `docs/02-proposal-package/project-plan.md` — Gantt and dependency view
4. `docs/02-proposal-package/wbs.md` — work-breakdown table
5. `docs/01-launch-packet/architecture-context.md` — system-context diagram (Mermaid)
6. `docs/01-launch-packet/screenshots/05-architecture-rendered.png` — rendered PNG fallback
7. `docs/ai-use-log.md` — audit table
8. `engineering-log.md` — process evidence

A pre-rendered PNG of the Gantt chart should be saved at `docs/02-proposal-package/screenshots/gantt.png` before recording (generated from `scripts/render_gantt.py`).

---

# Script

Total budget: **~15:00**. Each segment lists its time slot, on-screen cue, and narration. Read aloud at ~150 words per minute; the narration counts below assume that pace.

---

## Segment 1 — Opening and roadmap (0:00 – 1:00, 1 min)

**Show on screen:** `README.md` open at the top, title visible.

**Narration (~140 words):**

> "Hi, I'm Zixuan Liang. This is the Week 2 walkthrough for my CISC 699 applied project, SafeExec — a hardened, threat-modeled Python execution sandbox for LLM-agent tool-use. I'll spend the next fifteen minutes walking through five things: first, the problem I'm solving and why it's a real CS problem worth fourteen weeks; second, the proposal's scope and the trade-offs I made to get there; third, the feasibility evidence across the MACP layers — machine, architectures, computational method, and API; fourth, the project plan and the critical-path chain I'm committing to; and fifth, my risk and ethics posture plus my AI-use discipline. I'll close with what I'm asking my supervisor to approve and what comes next. The proposal document itself is in this repo at `docs/02-proposal-package/proposal.md`; everything I'll show on screen is linked from there."

**On-screen action:** Click into `docs/02-proposal-package/proposal.md` and scroll briefly to show the table of contents area.

---

## Segment 2 — Problem framing and significance (1:00 – 3:00, 2 min)

**Show on screen:** `proposal.md` §§2–3 (Background and Problem statement). Optionally open OWASP and NIST source pages briefly in adjacent tabs.

**Narration (~290 words):**

> "Here's the problem. LLM-powered software agents — Claude Code, Code Interpreter, Cursor, Devin, an expanding open-source ecosystem — increasingly execute model-generated Python code as part of their tool-use loop. The executor is the layer where text becomes program execution on real infrastructure. In production, that layer is the one most often built quickly and revisited never. Most open-source agents today execute model output inside their own process tree, or inside a Docker container with default settings and a permissive network policy. Neither is a defensible posture when the code being executed was produced by a language model under conditions of possible prompt injection."
>
> "This is not a hypothetical concern. NIST AI 100-2's 2025 update names tool-execution isolation as an under-specified mitigation surface. OWASP's 2025 LLM Top 10 calls out sandboxed execution explicitly in LLM05, 'Improper Output Handling,' and in LLM06, 'Excessive Agency.' Real container-escape vulnerabilities continue to be discovered in widely deployed runtimes — runc CVE-2019-5736, runc CVE-2024-21626 — confirming that 'default Docker' isn't a defensible posture."
>
> "What already exists: closed-source services like Anthropic's analysis tool and OpenAI's Code Interpreter address these risks behind opaque infrastructure. The open-source landscape has one strong commercial-backed option in E2B, which uses Firecracker microVMs, and a handful of lighter projects that ship convenience but not measured isolation strength. None of those open-source projects publishes a documented threat model paired with a reproducible adversarial benchmark. That gap — a measurement framework, not a new isolation primitive — is what SafeExec contributes."

**On-screen action:** Highlight or scroll past the problem-statement paragraph in `proposal.md` §3.

---

## Segment 3 — Candidates considered and selection rationale (3:00 – 5:00, 2 min)

**Show on screen:** `docs/01-launch-packet/candidate-projects.md` — the comparison matrix.

**Narration (~290 words):**

> "I considered three candidate projects before committing to this one. Candidate A was a domain-specialized coding agent paired with a self-built benchmark — well-understood evaluation methodology, low technical risk, but one step removed from the kind of infrastructure work I want my portfolio to show. Candidate B was a multi-model agent router optimizing cost, quality, and latency — interesting but a crowded product space and harder to differentiate as a research artifact. Candidate C is SafeExec — a hardened Python execution sandbox with two isolation back-ends and a curated adversarial benchmark. The comparison matrix is in `docs/01-launch-packet/candidate-projects.md`."
>
> "I chose C for four reasons, in roughly this order of weight. First, portfolio fit: I'm targeting software-engineering roles at frontier AI labs on agent-tooling teams, and SafeExec is a credible miniature of the kind of infrastructure those teams build. Second, rubric fit: the CISC 699 evaluation rubric weights 'evaluation and evidence' heavily, and C's central contribution *is* an evaluation methodology — a forty-plus-program adversarial benchmark plus an A/B comparison across back-ends. That scores higher on the rubric levels that reward rigorous evaluation than A or B do, where the evaluation is borrowed from existing benchmarks. Third, ethics and broader impact: prompt injection, dual-use, agent misuse — those concerns are central to C, not tacked on. And fourth, the Python-only / no-network / no-GPU scope keeps both the threat model and the 14-week timeline honest. No model training. No specialized hardware. No fourteen-week scope creep."

**On-screen action:** Briefly scroll the comparison matrix; pause on the "Worst-case failure mode" row.

---

## Segment 4 — Scope and the scope-fence (5:00 – 6:30, 1:30 min)

**Show on screen:** `proposal.md` §8 (Scope) — show both the In-scope list and the Out-of-scope list.

**Narration (~220 words):**

> "Scope. In-scope: Python 3.11 user code, synchronous request-response API, ephemeral per-request filesystem, the standard resource limits — CPU, memory, wall-clock, PIDs, file descriptors — two back-ends, hardened Docker and gVisor, on a Linux x86-64 host. Out-of-scope, explicitly: no multi-language support, no network access from inside the sandbox, no GPU, no persistence across requests, no multi-tenant security, no production-grade auth or TLS, no Windows or macOS, no Firecracker — Firecracker is a stretch only — no side-channel or hardware-level attacks, no nation-state adversaries. That out-of-scope list is the part most worth reading carefully, because the scope-fence policy in §8.3 says the in/out split is fixed from W3 through W8. The only sanctioned re-scoping moment is the Week 7 midpoint review. Outside that window, the default is no change. That's deliberate — the worst-case failure mode for a project like this is scope creep into multi-language or persistence features, and the scope-fence is the explicit mitigation for that risk. I named the risk as R1 in the register, and the W7 checkpoint is the matching contingency."

**On-screen action:** Highlight §8.3 (scope-fence policy) and pause briefly.

---

## Segment 5 — Feasibility evidence across the MACP layers (6:30 – 9:00, 2:30 min)

**Show on screen:** `proposal.md` §9 (MACP framing) — scroll through 9.1, 9.2, 9.3, 9.4 in order. Have `engineering-log.md` open in an adjacent tab to show the W1 droplet inventory.

**Narration (~370 words):**

> "Feasibility across the MACP layers — machine, architecture, computational method, API."
>
> "Machine. I provisioned a DigitalOcean Premium Intel droplet on May 17, two vCPU, four gigs of RAM, Ubuntu 22.04 LTS, kernel 5.15. Docker 29.5.0 and gVisor's runsc release-20260511 are already installed. Total compute budget envelope is $150 to $250 across the term, well inside the charter's $400 ceiling. The droplet output is in the engineering log under the May 17 entry — `uname -r`, `cat /etc/os-release`, `docker version`, `runsc --version`."
>
> "Architecture. The system-context diagram is in `docs/01-launch-packet/architecture-context.md`. It commits the project to four load-bearing decisions: two back-ends not one, a single execution API, the threat model as a first-class deliverable, and external LLM only for the demo. The detailed component design — the Sentry-Gofer flows inside gVisor, the seccomp filter inside the Docker container, the cgroup hierarchy — is W4 work, captured in `docs/design/architecture.md`."
>
> "Computational method. The isolation primitives are well-established. Hardened Docker is OS-level container isolation with seccomp filters, AppArmor profiles, dropped capabilities, and cgroup-enforced limits. gVisor is user-space syscall interposition — its Sentry component implements its own kernel surface in Go, so the host kernel attack surface visible to the application is dramatically reduced. The evaluation method for the functional suite is deterministic output comparison — byte-equality of stdout and stderr against a reference CPython 3.11 interpreter, which is the same methodological model SWE-bench uses for its graders."
>
> "API integrations. Anthropic's Claude API for the reference-agent demo only — a ≤50-line agent, budget ~$30 to $50. Docker Hub for base images. GitHub for source. HumanEval and MBPP, both permissively licensed, for the functional-corpus seed. gVisor's apt repo for runsc. No other third-party SaaS in scope. Every one of these integrations has a named failure mode in §9.4 with a contingency."

**On-screen action:** Briefly scroll the architecture diagram (PNG) and the MACP §9 table.

---

## Segment 6 — Project plan, gates, and the critical path (9:00 – 11:30, 2:30 min)

**Show on screen:** `project-plan.md` §§2 (Gantt) and §4 (Critical path). Have `wbs.md` open in an adjacent tab.

**Narration (~360 words):**

> "Project plan. Fourteen weeks, six phases, six explicit completion gates. The Gantt in `project-plan.md` shows them: G1 at W2 — this proposal, target approval by May 26. G2 at W4 — the design review for architecture, threat model, and evaluation plan. G3 at W5 — first end-to-end Python execution under the Docker baseline. G4 at W7 — midpoint demo and the only sanctioned scope-renegotiation point in the whole term. G5 at W11 — full report draft to my supervisor. G6 at W14 — final submission."
>
> "The critical path is G1 → G2 → G3 → G4 → W8 gVisor → G5 → G6. Any slippage on any link is a slip risk for the deliverable. I've built in two named relief valves. First, if hello-world execution misses the W5 gate, the contingency at June 19 activates — W6 becomes combined execution-plus-hardening, and that gets flagged as a W7 topic. Second, if the W7 midpoint shows fewer than fifty functional programs passing or fewer than ten adversarial programs working, the scope falls back to Docker-only and W8 redirects to adversarial-suite expansion. Those are pre-committed responses, named in §10.5 so the response isn't improvised under pressure."
>
> "The WBS in `wbs.md` decomposes this into about thirty leaf tasks, each mapped to a week, to a deliverable, and to a success criterion in §7. The total estimate is about 272 student-hours across 14 weeks — about 17 to 20 hours a week. The W1 feasibility memo had it at 235; the 272 figure includes the contingency buffer. Every task maps to at least one success criterion. Every success criterion is covered by at least two tasks. The instructor's self-check — 'can every task in your plan be traced to a success criterion' — is satisfied."

**On-screen action:** Open the Gantt PNG (or scroll the Mermaid source); highlight the W5 and W7 gates; scroll briefly through the WBS table to show the SC column.

---

## Segment 7 — Risks, ethics, and AI-use discipline (11:30 – 13:30, 2 min)

**Show on screen:** `proposal.md` §12 (Risk register), §14 (Ethics), §17 (AI-use); then briefly `docs/ai-use-log.md`.

**Narration (~290 words):**

> "Risks. Twelve named in the register, each with likelihood, impact, mitigation, owner, and contingency. The four with the highest expected cost are: scope creep — addressed by the scope-fence in §8.3 and the W7 checkpoint; adversarial-suite quality — addressed by category lock at W3 and midpoint peer review; gVisor performance variability — addressed by the pre-registered benchmark protocol with percentile reporting; and AI-use disclosure gaps — which leads me to the academic-integrity point."
>
> "Ethics. The adversarial suite is dual-use — it contains programs that probe for isolation failures. I'm publishing it anyway, because a benchmark that can't be reproduced can't be trusted, and the alternative is a claim no one can verify. I'm mitigating the dual-use concern in three ways: every adversarial program targets *only* SafeExec; the category-level taxonomy is published in the threat model, but per-program details are released only with the W14 artifact; and the report's broader-impact section will explicitly state the trade-off."
>
> "AI-use. My Week 1 packet was graded 90 out of 100. The four-of-five dimensions at Level 1 was good; the AI-use log was at Level 2 — 15 of 20. The feedback was that the log was descriptive rather than audit-oriented. I restructured it on May 18 into the per-artifact audit-table format you can see in `docs/ai-use-log.md` — tool, purpose, prompt summary, authorship label, extent of student modification — plus an explicit enumeration of student-only decisions. Every artifact in this W2 package carries an inline disclosure block at the top, and the audit table now has entries for every new W2 document."

**On-screen action:** Briefly open `docs/ai-use-log.md` to show the audit table; close it.

---

## Segment 8 — What I'm asking, and what's next (13:30 – 15:00, 1:30 min)

**Show on screen:** `approval-brief.md` open at the top; then close to `README.md`.

**Narration (~220 words):**

> "What I'm asking my supervisor to approve at this hard stop. The one-page approval brief in `approval-brief.md` says: approved means scope, contribution framing, success criteria, project plan with gates, risk register, AI-use discipline, and reproducibility commitment. Conditional means the four supervisor questions from the W1 briefing: framing acceptability, open-source release timing, the reference-agent demo, and meeting cadence. Evidence expected by the W4 design review: requirements document, detailed architecture, threat model, evaluation plan, bibliography expanded to at least ten sources, and the engineering log kept current."
>
> "If the supervisor signals any of the four conditional items should change, the affected sections of `proposal.md` get revised before W3 begins, the revisions land in the engineering log, and we re-circulate."
>
> "Next steps if approval lands: I begin W3 lit-synthesis and requirements drafting on the assumption of approval. The next graded hard stop is the W7 midpoint, which is also the only sanctioned scope-renegotiation moment. Between now and then, the engineering log is the running record."
>
> "That's the walkthrough. Thanks for watching. Everything I covered is in the repo at github.com/liangzixuan/cisc-699 under `docs/02-proposal-package/`."

**On-screen action:** Close all tabs, leave `README.md` visible with the W2 section linked. Stop recording.

---

# Pre-recording checklist

Run through this list within 24 hours before recording to avoid the most common failure modes:

- [ ] Microphone level tested; play back the first 30 seconds.
- [ ] All eight source files open as tabs in a fresh browser window or IDE.
- [ ] Notifications muted; calendar reminders silenced; Slack/Discord set to Do Not Disturb.
- [ ] Pre-rendered Gantt PNG saved at `docs/02-proposal-package/screenshots/gantt.png`.
- [ ] Architecture PNG visible (already at `docs/01-launch-packet/screenshots/05-architecture-rendered.png`).
- [ ] Camera framing rehearsed; lighting OK; background neutral.
- [ ] Water within arm's reach.
- [ ] One short rehearsal pass (read segments 1–3 aloud, time check).

# Post-recording checklist

- [ ] Video runtime ≤16:00; ideally 14:30–15:30.
- [ ] Audio audible end-to-end; no dropouts.
- [ ] Renamed `safeexec-w2-walkthrough.mp4`; saved under `docs/02-proposal-package/recording/` (or to the cloud destination if file size is large).
- [ ] Uploaded to Canvas (media field or YouTube unlisted link in text entry); upload confirmed.
- [ ] AI-use log updated with a row for this recording (Authorship label: Student-only for the spoken delivery; AI-drafted, student-revised for this script).
- [ ] Engineering log entry under W2 noting the recording date and any retakes.

---

*End of walkthrough script.*
