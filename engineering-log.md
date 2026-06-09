# Engineering Log

Process evidence for CISC 699. One entry per working session — terse is fine, decisions and blockers are the point.

Conventions: one heading per week; under it, dated bullets. Mark decisions with **[DECISION]**, blockers with **[BLOCKER]**, scope changes with **[SCOPE]**, AI assistance with **[AI]**.

---

## Week 1 (2026-05-09 → 2026-05-15)

### 2026-05-13
- Repo initialized at `/Users/ericliang/PycharmProjects/CISC-699/`. Folder structure set up: `docs/`, `src/`, `tests/{functional,adversarial,performance}/`, `benchmarks/`, `deploy/`, `scripts/`.
- **[DECISION]** Project topic selected: hardened Python execution sandbox for LLM agent tool-use. See `docs/01-launch-packet/candidate-projects.md` for the three-candidate comparison that fed this decision.
- **[DECISION]** Initial scope locked to Python-only, no network, no GPU, single-tenant, Linux host. Rationale: keeps the threat model defensible and the 14-week timeline credible.
- **[DECISION]** Two isolation back-ends in scope: hardened Docker (baseline, W5–W6) and gVisor (W7–W8). Firecracker microVMs are a W10 stretch goal only if ahead of schedule.
- **[AI]** Used Claude (Sonnet 4.6 via Cowork) to scaffold repo structure, draft initial problem statement, draft project charter, draft three-candidate comparison. All AI output requires student review and revision before submission. See `docs/ai-use-log.md`.
- **[AI]** Annotated bibliography draft populated to 7 entries (≥5 W1 minimum met) via Claude-assisted web search + web fetch. Each entry grounded in a fetched primary source with explicit verification-status line naming what the student must still verify independently. Sources span all five planned categories. See `docs/ai-use-log.md` "W1 — Annotated bibliography draft" entry for the full log of searches run and URLs fetched.

### 2026-05-14
- **[AI]** Completed remaining W1 launch-packet artifacts: architecture/context diagram (Mermaid + scope-boundary explanation), substantive feasibility memo with six explicit student decisions (D1–D6), W2 issue-tracker seed (17 pre-drafted issues), workspace-screenshots checklist, and Git-push instructions.
- **[DECISION]** Initial commit landed locally: `2a280e6` tagged `w1-initial`. Author configured as Zixuan Liang <zliang1@my.harrisburgu.edu>. **Push to GitHub remote is student-only** (needs credentials); see `docs/01-launch-packet/git-push-instructions.md`.
- All five items in the launch packet's "Suggested submission package" are now drafted: charter, bibliography, feasibility memo, architecture/context sketch, screenshots checklist (screenshots themselves are student action).
- Next (student-only): voice revision pass on charter + bibliography; resolve feasibility-memo decisions D1–D6; capture screenshots; push to GitHub; populate issue tracker; submit to Canvas by Sunday 2026-05-17 11:59pm.

### 2026-05-17
- [x] Review and revise `project-charter.md` into own voice
- [x] Bibliography: complete the per-entry verification-reading items for the 7 drafted sources (each entry's "Verification status" line names what's still owed); revise annotations into own voice
- [x] Complete `feasibility-memo.md` (data, compute, software deps, deployment, time)
- [x] Complete `supervisor-briefing.md` (advisor briefing; decisions still needed from Prof. Lateef)
- [x] Initialize Git repo and push to private GitHub remote
- [x] Create issue tracker (GitHub Issues) with W2 charter-approval tasks
- [x] Submit launch packet to Canvas
- [x] the advisor briefing was emailed to Prof. Lateef and Dr. Shaalan on the same day

DigitalOcean droplet
```
ssh root@142.93.68.153
```

uname -r
```
5.15.0-179-generic
```

cat /etc/os-release | head -3
```
PRETTY_NAME="Ubuntu 22.04.5 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
```

start a tmux session to keep long-running commands going if your SSH session drops
```
tmux new -s safeexec
```

DigitalOcean Premium Intel droplet, NYC3, 2 vCPU / 4 GB / 120 GB NVMe
Ubuntu 22.04.5 LTS
Linux kernel: <output of `uname -r`>
Docker: 29.5.0
runsc: release-20260511.0 (OCI spec 1.2.1)

=== W1 droplet inventory (2026-05-17T21:06:18Z) ===
Linux safeexec-dev 5.15.0-179-generic #189-Ubuntu SMP Tue May 5 18:20:56 UTC 2026 x86_64 x86_64 x86_64 GNU/Linux
Description:    Ubuntu 22.04.5 LTS
Docker version 29.5.0, build 98f1464
runsc version release-20260511.0
spec: 1.2.1

{
    "runtimes": {
        "runsc": {
            "path": "/usr/bin/runsc"
        }
    }
}

---

## Week 2 (2026-05-16 → 2026-05-22)

### 2026-05-18
- **W1 launch packet graded: 90/100.** Four of five rubric dimensions at Level 1 (Advanced/Exceptional 90–100%); AI Usage Log at Level 2 (15/20). Professor's specific feedback: log was descriptive rather than audit-oriented; in-text attribution inconsistent; needs artifact-level disclosure notes, table of tool/purpose/prompts/extent, explicit statements of human-authored decisions, consistent inline acknowledgment conventions.
- **[DECISION]** Strengthen AI-use disclosure now (regardless of whether resubmission is allowed) because (a) the log is a living document carried through W14, (b) if resubmission is permitted this is the most-worth-resubmitting artifact, (c) the disclosure rigor needs to be in place before the W11/W14 report's AI-use appendix is assembled.
- **[AI]** Used Claude (Sonnet 4.6 via Cowork) to restructure `docs/ai-use-log.md` into audit-oriented format per the professor's specific improvement suggestions: per-artifact table with tool/purpose/prompt-summary/extent-of-modification columns, decision-authorship taxonomy (Student-originated / AI-drafted-student-revised / AI-drafted-student-accepted / AI-advised-student-executed / Student-only), explicit enumeration of Student-only decisions, ongoing-disclosure process for W2-W14 including commit-message AI-use trailers and code-level annotations.
- Added inline AI-use disclosure blocks at the top of each W1 artifact (problem-statement, candidate-projects, project-charter, feasibility-memo, annotated-bibliography, architecture-context, supervisor-briefing, w2-github-issues, screenshots-checklist, git-push-instructions). Each block names the tool, the authorship label, the document-specific human-authored decisions, and links to the audit log.
- Other professor improvement items captured for W3-W4 work (not addressed in this W2 sweep): explicit measurable research questions/hypotheses, quantified success metrics, formal risk register, contingency milestones for high-risk components, peer-reviewed source expansion, citation-format tightening, expanded stakeholder analysis. These belong in `docs/design/requirements.md` (W3), `docs/design/architecture.md` + `docs/design/threat-model.md` + `docs/design/evaluation-plan.md` (W4), and the bibliography expansion toward the W11 ≥15-source target.

### 2026-05-21
- **W2 Proposal Approval Package assembled.** Five Markdown source files plus a consolidated 53-page DOCX and PDF, all under `docs/02-proposal-package/`. The package supersedes the W1 charter as the project's authoritative scope-and-plan document; the W1 charter file now carries a "Superseded" header note.
- **[DECISION]** Brought forward all W3-W4 W1-feedback items into the W2 proposal where the W2 rubric naturally covered them: measurable research questions/hypotheses (proposal §4); quantified success metrics (proposal §7 — six sub-tables with thresholds and measurement methods); formal risk register (proposal §12 — added likelihood/impact/owner/contingency columns); contingency milestones (proposal §10.5 — explicit fallback dates for the five highest-risk slips); expanded stakeholder analysis (proposal §15 — twelve named stakeholders with relationship, expectations, and what the project provides). This brings the proposal up against the Level-1 bar across every W2 rubric dimension and clears the equivalent items off the W3-W4 backlog so the design phase can focus on requirements/architecture/threat-model/evaluation-plan instead of revisiting framing.
- **[DECISION]** Adopted MACP framing as an explicit §9 in the proposal (Machine / Architectures / Computational method / API) per the W2 assignment's MACP requirement.
- **[DECISION]** Pre-rendered the Gantt chart as a static PNG with matplotlib (`scripts/render_gantt.py` to land in the repo at next commit) rather than relying on Mermaid; the rendered chart is embedded in the consolidated DOCX/PDF and the Mermaid source is preserved in `project-plan.md` §2 for graders who prefer to re-render.
- **[AI]** Used Claude (Sonnet 4.6 via Cowork) to draft the five W2 Markdown artifacts (proposal, project-plan, wbs, approval-brief, walkthrough-script) and to produce the consolidated DOCX via pandoc + the docx skill's pack/validate scripts. Authorship rows 17–23 in `docs/ai-use-log.md` §4a. Student-revised every numeric threshold, every contingency date, every risk rating, the W7 explicit scope-renegotiation framing, and the choice of which items in `approval-brief.md` belong in Approved / Conditional / Evidence-expected.
- **[DECISION]** The recorded walkthrough video (50 pts of the 100-pt rubric) will be recorded by the student against `walkthrough-script.md` before the Canvas deadline. The script is paced for 14:30–15:30; the production checklist is at the bottom of that file.
- Next: capture the recording; commit the W2 package; submit to Canvas before 2026-05-24 23:59 ET; await advisor sign-off by 2026-05-26.

---

## Week 3 (2026-05-23 → 2026-05-29)

### 2026-05-25
- **W3 Literature and Requirements Brief assembled.** Created `docs/03-lit-req-brief/literature-and-requirements-brief.md` plus DOCX/PDF Canvas-submission artifacts. The brief expands the source base to 18 references and includes synthesis themes, gap analysis, functional and non-functional requirements, use cases, domain constraints, source/data inventory, and a requirements traceability matrix.
- **[DECISION]** Kept W3 requirements aligned to the W2-approved scope: Python 3.11 only; single-tenant; no network egress; no GPU; ephemeral per-request filesystem; hardened Docker plus gVisor as the planned comparison; W7 remains the only sanctioned scope-negotiation point.
- **[DECISION]** Framed SafeExec's W3 contribution as "threat-modeled measurement of sandbox behavior for Python LLM-agent tool-use" rather than as a replacement for managed products such as OpenAI Code Interpreter, Anthropic code execution, E2B, or Modal Sandboxes.
- **[AI]** Used Codex (GPT-5, Codex desktop app) to synthesize public sources, draft the brief, create a local DOCX builder, export the PDF with LibreOffice, and visually QA rendered PDF pages with Poppler. Public web sources only; no confidential or regulated data entered into AI tools. Updated `docs/ai-use-log.md` with W3 rows.

### 2026-05-27
- **[DECISION]** Prof. Khalid Lateef confirmed the W3 requirements and the W7 gVisor fallback plan.
- **[DECISION]** Functional corpus will use subsets of HumanEval and MBPP, plus student-authored functional tests where needed for SafeExec-specific coverage.
- **[DECISION]** Requirement thresholds remain unchanged: >=99% functional pass rate; >=90% adversarial containment for hardened Docker; >=95% adversarial containment for gVisor; >=30 benchmark samples per condition.
- **[DECISION]** Adversarial-suite disclosure plan confirmed: publish category taxonomy early, publish full program details later with containment context.
- **[DECISION]** License/data handling: prefer upstream HumanEval and MBPP sources, record task IDs and provenance, preserve required license notices with any copied subset, and avoid vendoring full datasets unless needed for reproducibility.

### 2026-05-28
- **W2 proposal approval feedback received.** Feedback describes the package as exceptionally strong and likely mid-to-high Level 1 if walkthrough delivery matches the written materials. Strengths named: measurable success criteria, threat-model framing, disciplined scope boundaries, evaluation-first methodology, risk planning, reproducibility, contingency planning, and walkthrough-script ownership.
- **[RISK]** Primary concern is execution risk, not conceptual weakness: gVisor integration, adversarial benchmarking, and hardened runtime behavior are substantial for a single-student 14-week project.
- **[DECISION]** Treat the W2 proposal scope as approved and shift operating posture from documentation growth to execution discipline. W4 work should define benchmark rules and implementation details tightly; W5-W7 should prioritize runnable code, containment tests, and early fallback signals.

---

## Week 4 (2026-05-30 → 2026-06-05)

### 2026-05-30
- **W4 Design Review Package assembled.** Created `docs/04-design-review-package/design-review-package.md`, generated architecture/evaluation diagrams, and exported DOCX/PDF Canvas-submission artifacts. The package covers component responsibilities, build order, execution/data flow, API contract, Docker/gVisor method, environment/toolchain plan, corpus validation, benchmark protocol, risk controls, and W4 approval checklist.
- **[DECISION]** Kept the package implementation-facing per W2 feedback: W5 target is a first `POST /execute` hello-world request through the Docker backend; optional feature growth remains out of scope.
- **[AI]** Used Codex (GPT-5, Codex desktop app) to draft the package, generate diagrams with a local Python/Pillow builder, generate the DOCX/PDF, and render page PNGs for visual QA. Public course and repository artifacts only; no confidential or regulated data entered into AI tools.

---

## Week 5 (2026-06-06 → 2026-06-12)

### 2026-06-09
- **Implementation Sprint I baseline created.** Added `src/safeexec/` package with execution models, backend interface, dev-only local subprocess backend, Docker/gVisor command builder, service layer, CLI, and a stdlib JSON API shell for `POST /execute`.
- **[DECISION]** Use the `local` backend only as a reproducible development smoke-test shim. It is not a security boundary and cannot support containment claims. Docker/gVisor remain the approved target isolation path for W6-W8.
- **[DECISION]** Keep W5 dependency-free (Python standard library only) so `make smoke` and `make test` are reliable on the authoring machine before adding external framework or benchmark dependencies.
- Added baseline tests under `tests/functional/`: local execution success, timeout handling, API response shape, hardened-Docker command controls, and gVisor `runsc` runtime selection.
- Added `Makefile` targets: `make smoke`, `make test`, and `make api`. Captured W5 evidence in `docs/05-implementation-sprint-i/smoke-output.txt`, `test-output.txt`, and `benchmark-smoke-output.txt`.
- **[RISK]** Docker execution has not yet been run from this local workspace. W6 must run the Docker backend on the Ubuntu droplet and capture the first real containerized `POST /execute` evidence.
- **[RISK]** Functional corpus and adversarial suite are still seeds. W6 should add the first HumanEval/MBPP manifest entries and initial student-authored adversarial programs only after the Docker boundary is exercised.
- **[AI]** Used Codex (GPT-5, Codex desktop app) to scaffold the W5 code baseline, tests, check-in Markdown, README/log updates, and local evidence capture. Student must review command output and the generated DOCX/PDF before Canvas submission.
