# W2 Issue Tracker Seed

> **AI-use disclosure.** Drafted with Claude Sonnet 4.6 (Cowork desktop app). AI-drafted, student-accepted. Key human-authored actions: copy-paste of these issues into the actual GitHub Issues tracker; ongoing issue prioritization and re-sequencing as W2–W5 work proceeds. Full audit trail: [`docs/ai-use-log.md`](../ai-use-log.md).

**Purpose.** The launch packet requires the student to "create the project workspace: version-control repository, top-level folder structure, **issue tracker**, and a running engineering log." This file is the pre-drafted issue list to push to GitHub Issues (or a comparable tracker) once the remote exists. Copy each block into a new issue.

**How to use.**

1. `git push` to your GitHub remote (see `docs/01-launch-packet/git-push-instructions.md` if it exists, or your provider's standard remote-creation flow).
2. In the GitHub repository, **Settings → Features → Issues** must be enabled (it is, by default).
3. Create labels first (one-time setup): `w1`, `w2`, `w3`, `w4`, `w5`, `w7-midpoint`, `w11-draft`, `w13-freeze`, `w14-final`, `risk`, `scope`, `student-decision`, `supervisor-needed`, `feasibility`, `bibliography`, `charter`.
4. Create each issue below by pasting **Title** into the title field and **Body** into the description.

---

## W1 closeout (must close before Sunday 2026-05-17, 11:59pm)

### Issue 1 — Revise project charter into own voice

**Labels:** `w1`, `charter`
**Body:**
The project charter at `docs/01-launch-packet/project-charter.md` was AI-drafted. Read it end to end, rewrite any passage that doesn't sound like your own voice, verify every number (budget envelope, success-criteria thresholds, milestone dates) against your personal calendar and the syllabus. The graders read across many students and will recognize generic AI cadence. Cut adjectives; keep specifics.

Acceptance: final version has zero residual phrases like "yields a reusable methodology" or "well-curated"; dates match CLAUDE.md week-map; numbers are commitments you'd defend in a viva.

---

### Issue 2 — Complete annotated-bibliography verification reading

**Labels:** `w1`, `bibliography`
**Body:**
Each of the 7 bibliography entries in `docs/01-launch-packet/annotated-bibliography.md` has a "Verification status (2026-05-13)" line naming what was AI-verified vs. what's owed by the student. Close those gaps:

- [ ] [1] NIST AI 100-2 E2025 — read the GenAI chapter + prompt-injection / agent-misuse sections
- [ ] [2] OWASP LLM Top 10 2025 — read LLM01, LLM05, LLM06 detail pages
- [ ] [3] gVisor docs — read Security Model + Performance Guide subpages
- [ ] [4] Firecracker NSDI '20 — read the paper PDF (architecture + security sections)
- [ ] [5] E2B — locate and read E2B's own architecture/security docs at e2b.dev/docs
- [ ] [6] SWE-bench ICLR 2024 — read the paper
- [ ] [7] Red Hat CVE-2019-5736 — read at least one detailed technical writeup (AWS blog or Frichetten PoC)

After verification, revise each annotation into your own voice.

---

### Issue 3 — Resolve student decisions D1–D6 in feasibility memo

**Labels:** `w1`, `feasibility`, `student-decision`
**Body:**
`docs/01-launch-packet/feasibility-memo.md` flags six decisions (D1–D6) that need student input. Resolve each, update the memo to remove the `STUDENT DECISION` markers, and pre-write the supervisor questions for the W2 meeting:

- [ ] D1: Hand-authored functional corpus *or* HumanEval/MBPP subset reuse
- [ ] D2: Compute provider (Hetzner / DigitalOcean / AWS / local / HU lab)
- [ ] D3: Ubuntu 22.04 vs. 24.04 host
- [ ] D4: Repository visibility (private during term recommended)
- [ ] D5: Realistic weekly availability (≥12 hrs/week target)
- [ ] D6: Supervisor cadence and milestone meeting windows

---

### Issue 4 — Schedule the W2 supervisor meeting

**Labels:** `w1`, `supervisor-needed`
**Body:**
Per the charter milestone map, W2 (2026-05-16 → 2026-05-22) is charter-approval. Send the supervisor `docs/01-launch-packet/supervisor-briefing.md` (revised into own voice first — see Issue 1's voice pass) and request a 45-minute meeting. Confirm by 2026-05-20.

Pre-meeting checklist:
- [ ] Supervisor briefing sent
- [ ] Meeting scheduled
- [ ] Open questions (sec. 3 of the briefing) reviewed
- [ ] Decisions D1–D6 either resolved or queued for supervisor input

---

### Issue 5 — Take workspace screenshots

**Labels:** `w1`
**Body:**
See `docs/01-launch-packet/screenshots-checklist.md`. Capture the named screenshots into `docs/01-launch-packet/screenshots/` and reference them in the README.

Expected: 4–6 screenshots, ≤500KB each (PNG, downsized).

---

### Issue 6 — Export architecture diagram to static image

**Labels:** `w1`
**Body:**
`docs/01-launch-packet/architecture-context.md` ships a Mermaid diagram that renders on GitHub but not in a Canvas PDF or static PDF. Export via [mermaid.live](https://mermaid.live) (paste the code block, click "Actions → SVG" or "PNG"), save to `docs/01-launch-packet/architecture-context.svg`, and link from the README and from the launch-packet Canvas submission.

---

### Issue 7 — Push initial commit to private GitHub remote

**Labels:** `w1`
**Body:**
The local Git repository was initialized with all W1 artifacts staged in a single initial commit. Push to a new private GitHub repository (`gh repo create cisc-699-safeexec --private --source=. --push` if `gh` is installed, or manual remote setup otherwise). Add supervisor as collaborator. Verify the repo URL renders Markdown and Mermaid correctly.

---

### Issue 8 — Submit launch packet to Canvas

**Labels:** `w1`
**Body:**
The "01 Project Launch Packet" assignment is due Sunday 2026-05-17 11:59pm. Submit a single organized package:

- [ ] Project charter (PDF export of `project-charter.md`)
- [ ] Annotated bibliography (PDF)
- [ ] Feasibility memo (PDF)
- [ ] Architecture/context sketch (SVG/PNG from Issue 6)
- [ ] Workspace screenshots (from Issue 5)
- [ ] Repo URL
- [ ] Optional: problem-statement + candidate-projects + supervisor-briefing as supporting context

---

## W2 (2026-05-16 → 2026-05-22)

### Issue 9 — Run W2 charter-approval meeting with supervisor

**Labels:** `w2`, `supervisor-needed`
**Body:**
Hold the 45-minute charter-approval meeting. Outcomes captured in `engineering-log.md`:
- Charter approved (or revisions requested)
- Decisions D1–D6 resolved
- Supervisor cadence confirmed
- Open risks acknowledged

---

### Issue 10 — Revise charter post-supervisor feedback

**Labels:** `w2`, `charter`
**Body:**
Apply any supervisor-requested revisions from Issue 9. Tag the post-revision charter `v1.0` in Git. Going forward the charter is the contract; further changes require explicit supervisor sign-off.

---

### Issue 11 — Calendar-block W5, W7, W11, W13 checkpoints

**Labels:** `w2`
**Body:**
Block in personal calendar (not just project plan):
- W5 (week of 2026-06-08): "Hello world execution under hardened Docker" — go/no-go for gVisor path
- W7 (2026-06-26): Midpoint demo
- W11 (2026-07-24): Full report draft to supervisor
- W13 (week of 2026-08-04): Final freeze, AI-use appendix consolidation

These are commitments to the supervisor and the rubric; calendar visibility is a process discipline the rubric weights.

---

## W3 (2026-05-23 → 2026-05-29)

### Issue 12 — Literature / related-work synthesis (≥10 entries in bibliography)

**Labels:** `w3`, `bibliography`
**Body:**
Grow the bibliography from 7 (W1) entries toward 15 (W11 target). Specifically populate the gaps listed in the "Sources identified but not yet fetched" section of `annotated-bibliography.md`:
- [ ] Greshake et al. indirect prompt injection paper (or equivalent)
- [ ] Linux kernel seccomp_filter.txt primary doc
- [ ] gVisor Case Study (Young et al. HotCloud '19)
- [ ] CVE-2024-21626 "Leaky Vessels" technical writeup
- [ ] One agentic-eval benchmark paper (GAIA, AgentBench, ToolBench)

---

### Issue 13 — Requirements & use-case document

**Labels:** `w3`
**Body:**
Author `docs/design/requirements.md`. Sections: functional requirements (must/should/could), non-functional requirements (latency, throughput, isolation strength), use cases (UC-1 developer integration, UC-2 researcher running benchmark, UC-3 student authoring adversarial program).

---

## W4 (2026-05-30 → 2026-06-05)

### Issue 14 — Architecture deep-dive document

**Labels:** `w4`
**Body:**
Author `docs/design/architecture.md` — component-level design of API gateway, executor orchestrator, both back-ends, and the test-suite runners. Include sequence diagrams for a normal-case execution and an adversarial-case execution.

---

### Issue 15 — Threat model document

**Labels:** `w4`, `risk`
**Body:**
Author `docs/design/threat-model.md`. Required sections: actors, capabilities, in-scope attacks (mapped to OWASP LLM05/LLM06 categories), out-of-scope attacks (nation-state, side-channel, hardware), assumed-trustworthy components, residual risks. The W4 design review is the supervisor's checkpoint for this document.

---

### Issue 16 — Evaluation plan document

**Labels:** `w4`
**Body:**
Author `docs/design/evaluation-plan.md`. Required: functional-suite methodology, adversarial-suite category taxonomy with rationale, performance-benchmark protocol (warm-up iterations, sample sizes, percentile reporting, confidence-interval construction), statistical-analysis plan. Pre-register before W5 implementation begins — pre-registration is a credibility win.

---

## W5 implementation kickoff (2026-06-06 → 2026-06-12)

### Issue 17 — Project bootstrap: API skeleton + first hardened Docker container

**Labels:** `w5`
**Body:**
Land the minimal walking skeleton: FastAPI server with `POST /execute`, a single executor implementation calling a Docker container that runs Python, structured JSON response, ≥3 functional test programs passing. This is the W5 hard checkpoint named in the charter (R4 risk).

Acceptance criteria:
- `make setup && make test` runs to green on a stock Ubuntu 22.04 VM
- The Docker container runs as non-root with read-only rootfs and no network namespace
- The API returns `{stdout, stderr, exit_code, duration_ms, peak_mem_mb}` for a "print(1+1)" program

---

*Issues 18+ are added as W5+ work begins. Each opens an issue at the start of its week per standard process discipline.*
