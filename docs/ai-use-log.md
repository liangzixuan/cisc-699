# AI-Use Disclosure Log

**Owner:** Zixuan Liang
**Course:** CISC 699 — Applied Project in Computer Information Sciences (Summer 2026)
**Last updated:** 2026-06-26

## 1. Purpose and policy

This document is the authoritative audit trail of every substantive use of generative AI in this project. Per the CISC 699 syllabus, AI-generated text, code, analysis, or figures may not be submitted as unaided work, and all substantial AI assistance must be disclosed. This log is the source from which the W14 final-report AI-use appendix will be assembled.

The W1 launch-packet review feedback (received 2026-05-18) flagged that the prior version of this log was descriptive rather than audit-oriented. This revision adopts an explicit audit format: per-artifact attribution, decision-authorship labels, an enumeration of human-only decisions, and an ongoing-disclosure process for W2–W14.

**Excluded from AI systems at all times.** No confidential, proprietary, FERPA-regulated, HIPAA-regulated, personal, or otherwise restricted data has been entered into any AI tool used on this project. Only public course materials (the syllabus, the launch packet PDF) and student-authored project artifacts have been shared.

## 2. Decision-authorship taxonomy

The per-artifact table below uses these labels:

| Label | Meaning |
|---|---|
| **Student-originated, AI-articulated** | The student made the substantive choice; AI helped phrase or structure it. |
| **AI-drafted, student-revised** | AI produced an initial draft; the student substantially edited it (voice, framing, factual checks, sentence-level rewrites). |
| **AI-drafted, student-accepted** | AI produced a draft; the student reviewed and accepted with light or no changes. Used for boilerplate or technical-fact content. |
| **AI-advised, student-executed** | AI suggested an approach or command; the student carried it out and verified outputs. Used for shell commands, configuration steps, and tool selection. |
| **Student-only** | No AI assistance in any form. |

## 3. Inline disclosure conventions

Every substantive artifact in this repository carries a short AI-use block at the top of the file (immediately under the title) in the following format:

```markdown
> **AI-use disclosure.** Drafted with Claude Sonnet 4.6 (Cowork desktop app). <Authorship label>. Key human-authored decisions in this document: <list>. Full audit trail: [docs/ai-use-log.md](<relative-path>/docs/ai-use-log.md).
```

The block is intentionally short (2–3 lines) so the document remains readable; per-document detail lives in this log's audit table. Commit messages that include AI-assisted content append an `AI-use:` trailer line.

## 4. Audit table — W1 launch packet (2026-05-13 to 2026-05-17)

| # | Artifact | Tool | Purpose | Prompts / tasks (summary) | Authorship label | Extent of student modification |
|---|---|---|---|---|---|---|
| 1 | `README.md` | Claude Sonnet 4.6 (Cowork) | Initial draft of living grading-doc overview | "Initial README with project framing, status, repo layout, AI-use note" | AI-drafted, student-revised | Student edited the W1 launch-packet index, status-table dates, and license note; added the GitHub URL after creating the remote |
| 2 | `engineering-log.md` | Claude Sonnet 4.6 (Cowork) | Initial structure + W1 seed entries | "Weekly engineering journal with W1 seed entry; conventions for [DECISION], [BLOCKER], [SCOPE], [AI] tags" | AI-drafted, student-accepted (structure); ongoing entries student-only | Student is sole author of entries from W2 onward |
| 3 | `.gitignore` | Claude Sonnet 4.6 (Cowork) | Standard Python/IDE/Docker ignore patterns | "Standard ignore patterns" | AI-drafted, student-accepted | Boilerplate; reviewed and accepted as-is |
| 4 | `.gitattributes` | Claude Sonnet 4.6 (Cowork) | Line-ending + binary-file rules + linguist markers | "Standard gitattributes" | AI-drafted, student-accepted | Boilerplate; reviewed and accepted as-is |
| 5 | `docs/01-launch-packet/problem-statement.md` | Claude Sonnet 4.6 (Cowork) | One-paragraph problem statement | "Draft a one-paragraph statement framing the LLM-agent sandbox motivation; identify stakeholders and what the project does and does not claim to solve" | AI-drafted, student-revised | Student revised wording, removed verbose preamble, verified empirical claims against bibliography sources |
| 6 | `docs/01-launch-packet/candidate-projects.md` | Claude Sonnet 4.6 (Cowork) | Three-candidate comparison + selection rationale | "Compare candidates A/B/C on feasibility, novelty, fit; argue selection of C given background and career objective" | Student-originated, AI-articulated (selection); AI-drafted, student-revised (comparison) | The choice of Candidate C was a student decision after AI presented options; AI drafted the comparison-matrix structure |
| 7 | `docs/01-launch-packet/project-charter.md` | Claude Sonnet 4.6 (Cowork) | Full charter (rationale, artifact, users, goals, scope, assumptions, stakeholders, risks, success criteria, milestone map) | "Draft charter with all standard sections; align dates to syllabus W1–W14; include risk register" | AI-drafted, student-revised | Student verified every milestone date against syllabus; revised scope §5 to reflect final commitments; reviewed and accepted success-criteria thresholds |
| 8 | `docs/01-launch-packet/feasibility-memo.md` | Claude Sonnet 4.6 (Cowork) | Substantive feasibility analysis flagged with 6 student-decision markers | "Replace outline stub with substantive content; flag D1–D6 as items requiring student input" | AI-drafted, student-revised | Student resolved all six decisions personally (D1–D6); student-verified cloud-provider pricing at signup; student removed verbose preamble |
| 9 | `docs/01-launch-packet/annotated-bibliography.md` | Claude Sonnet 4.6 (Cowork) + WebSearch + web_fetch tools | 7 IEEE-formatted annotations grounded in fetched primary sources | "Search for sources across 5 categories; fetch primary sources; draft annotations grounded only in fetched content; do not fabricate citations" | AI-drafted, student-revised | Student independently re-fetched and read each of the 7 sources; updated each "Verification status" line to first-person student voice; removed verbose preamble |
| 10 | `docs/01-launch-packet/architecture-context.md` | Claude Sonnet 4.6 (Cowork) | Mermaid system-context diagram + scope-boundary explanation | "Produce one system-context diagram + a short explanation of scope boundaries; map to charter §5" | AI-drafted, student-revised | Student exported diagram to PNG for Canvas; verified boundary alignment with charter §5 |
| 11 | `docs/01-launch-packet/supervisor-briefing.md` | Claude Sonnet 4.6 (Cowork) | 3-minute-read briefing requesting D1–D6 input | "Draft briefing memo with decisions, clarifications, risks for supervisor's read" | AI-drafted, student-revised | Student updated salutation (Prof., not Dr.), name, recipient list (added Prof. Lateef); revised §5 to remove stale W2 items |
| 12 | `docs/01-launch-packet/w2-github-issues.md` | Claude Sonnet 4.6 (Cowork) | 17 pre-drafted W2–W5 issues | "Pre-draft issues with titles, labels, bodies; copy-paste-ready" | AI-drafted, student-accepted | Student copy-pasted issues into the actual GitHub Issues tracker |
| 13 | `docs/01-launch-packet/screenshots-checklist.md` | Claude Sonnet 4.6 (Cowork) | Required-screenshot list with capture commands | "List required screenshots with rationale per launch-packet evidence requirement" | AI-drafted, student-accepted | Student captured all 5+1 screenshots themselves (the artifacts are Student-only) |
| 14 | `docs/01-launch-packet/git-push-instructions.md` | Claude Sonnet 4.6 (Cowork) | Two procedures (gh CLI, web UI) for pushing to GitHub | "Document gh CLI + web-UI push procedures" | AI-drafted, student-accepted (instructions); Student-only (execution) | Student executed the push, chose repo name `liangzixuan/cisc-699`, set public visibility |
| 15 | `docs/ai-use-log.md` (this file) | Claude Sonnet 4.6 (Cowork) | Audit-oriented disclosure log per professor's W1 feedback | "Restructure log to per-artifact table with authorship labels; add 'human-only decisions' section; define ongoing process" | AI-drafted, student-revised | Student reviewed every row for accuracy against actual workflow; ongoing entries student-only |

## 4a. Audit table — W2 proposal-approval package (2026-05-21)

| # | Artifact | Tool | Purpose | Prompts / tasks (summary) | Authorship label | Extent of student modification |
|---|---|---|---|---|---|---|
| 17 | `docs/02-proposal-package/proposal.md` | Claude Sonnet 4.6 (Cowork) | Formal proposal document superseding W1 charter; W2 rubric-aligned; MACP-framed | "Restructure W1 charter for W2 rubric and MACP framing; add measurable RQs and hypotheses; add contingency milestones; add formal risk register columns (likelihood/impact/owner/contingency); expand stakeholder analysis per W1 grading feedback; add Gantt and WBS pointers" | AI-drafted, student-revised | Student set every scope boundary in §8, every numeric threshold in §7, every risk likelihood/impact rating in §12, the W7 scope-renegotiation checkpoint, and every contingency date in §10.5 |
| 18 | `docs/02-proposal-package/project-plan.md` | Claude Sonnet 4.6 (Cowork) | Project plan appendix — Gantt source, dependency graph, gates, critical path | "Produce phase overview, Mermaid gantt source, dependency view, completion-gate table, critical path narrative" | AI-drafted, student-revised | Student approved gate dates against the syllabus and W1 charter; student is sole authority on the W7 'only sanctioned scope-renegotiation point' framing |
| 19 | `docs/02-proposal-package/wbs.md` | Claude Sonnet 4.6 (Cowork) | Work-breakdown structure with traceability to success criteria | "Produce WBS with per-task hour estimate, week, deliverable, success-criterion mapping, blocking dependencies; verify every task traces to a success criterion" | AI-drafted, student-revised | Student approved hour estimates against the W1 feasibility-memo total; student approved the SC mapping for every row |
| 20 | `docs/02-proposal-package/approval-brief.md` | Claude Sonnet 4.6 (Cowork) | One-page approval brief (rubric task 8) | "Produce one-page approval brief: what's approved, what's conditional, what evidence is expected by next checkpoint (W4)" | AI-drafted, student-revised | Student set which items belong in 'Approved', 'Conditional', and 'Evidence expected'; these are commitments to the supervisor |
| 21 | `docs/02-proposal-package/walkthrough-script.md` | Claude Sonnet 4.6 (Cowork) | ~15-minute script for the rubric's 50-pt recorded walkthrough | "Produce a per-segment script with minute budget, on-screen cues, narration text; cover problem framing, charter, scope, MACP feasibility, project plan, risks/ethics, AI-use, ask" | AI-drafted, student-revised | Student pace-tested the timing in a rehearsal pass; student is sole speaker on the recording (Authorship label for the recording itself is Student-only for delivery) |
| 22 | `docs/02-proposal-package/Proposal-Approval-Package.docx` | docx-js via `mcp__workspace__bash` | Consolidated Canvas-submission DOCX | "Assemble single submission-ready DOCX from proposal.md + appendices using the docx skill's docx-js patterns" | AI-advised, student-executed (file generation by tool); content authorship per rows 17–21 | Student reviews the rendered DOCX/PDF before Canvas upload; student is responsible for the final submission file |
| 23 | `docs/02-proposal-package/Proposal-Approval-Package.pdf` | LibreOffice (`soffice` headless) | PDF export of the consolidated DOCX | "Convert DOCX to PDF for Canvas attachment" | AI-advised, student-executed | Same as row 22 |

## 4b. Audit table — W3 literature and requirements brief (2026-05-25)

| # | Artifact | Tool | Purpose | Prompts / tasks (summary) | Authorship label | Extent of student modification |
|---|---|---|---|---|---|---|
| 24 | `docs/03-lit-req-brief/literature-and-requirements-brief.md` | Codex (GPT-5, Codex desktop app) + public web browsing | Literature synthesis, requirements, use cases, constraints, source/data inventory, and traceability matrix for the W3 assignment | "Use the Canvas assignment screenshot and existing W1/W2 artifacts to produce the Literature and Requirements Brief; expand sources; map literature to requirements and evidence; preserve advisor/instructor roles" | AI-drafted, student-revised | Student must verify final source inclusion, every requirement threshold, acceptance-evidence mappings, and advisor-review checklist before Canvas submission |
| 25 | `scripts/build_lit_req_brief.py` | Codex (GPT-5, Codex desktop app) | Local builder that converts the W3 Markdown master into DOCX with tables and embedded architecture image | "Generate a simple python-docx builder for the W3 brief, preserving headings, tables, bullets, code spans, links, and image insertion" | AI-drafted, student-accepted | Utility script only; student reviews generated DOCX/PDF rather than submitting the script |
| 26 | `docs/03-lit-req-brief/Literature-and-Requirements-Brief.docx` | `python-docx` via `scripts/build_lit_req_brief.py` | Canvas-ready DOCX for the W3 brief | "Build DOCX from Markdown master and visually inspect output" | AI-advised, student-executed (file generation by tool); content authorship per row 24 | Student reviews rendered document before Canvas upload |
| 27 | `docs/03-lit-req-brief/Literature-and-Requirements-Brief.pdf` | LibreOffice (`soffice` headless) + Poppler (`pdftoppm`) | PDF export and page-render QA of the W3 brief | "Convert DOCX to PDF; render representative pages to PNG to verify layout" | AI-advised, student-executed | Student reviews PDF before Canvas upload; render QA checked title/control, diagram/use-case, requirements, inventory, traceability, and references pages |

## 4c. Audit table — W4 design review package (2026-05-30)

| # | Artifact | Tool | Purpose | Prompts / tasks (summary) | Authorship label | Extent of student modification |
|---|---|---|---|---|---|---|
| 28 | `docs/04-design-review-package/design-review-package.md` | Codex (GPT-5, Codex desktop app) | Consolidated W4 design review package covering architecture, method, environment, API, testing/evaluation, risk controls, and AI-use note | "Use the W4 Canvas assignment screenshot, W2 approval feedback, W2 proposal, and W3 requirements to produce an implementation-facing design review package" | AI-drafted, student-revised | Student should verify final API contract, benchmark protocol, and W5 execution target before Canvas submission |
| 29 | `scripts/build_design_review_package.py` | Codex (GPT-5, Codex desktop app) | Local builder that generates diagrams and converts the W4 Markdown master into DOCX | "Create reproducible Python builder using python-docx and Pillow; apply standard business brief styling; render diagrams as PNGs" | AI-drafted, student-accepted | Utility script; student reviews generated artifacts rather than submitting the script |
| 30 | `docs/04-design-review-package/diagrams/*.png` | Codex-generated Python/Pillow drawing script | Component architecture and evaluation-flow diagrams | "Generate simple architecture and evaluation diagrams from the W4 package design" | AI-drafted, student-revised | Diagrams visually QA'd in rendered DOCX pages |
| 31 | `docs/04-design-review-package/Design-Review-Package.docx` | `python-docx` via local builder | Canvas-ready DOCX for W4 Hard Stop 2 | "Build DOCX from Markdown master and generated diagrams" | AI-advised, student-executed; content authorship per rows 28-30 | Rendered to PNG pages for layout QA |
| 32 | `docs/04-design-review-package/Design-Review-Package.pdf` | LibreOffice (`soffice` headless) | PDF export of W4 design review package | "Convert DOCX to PDF for Canvas submission" | AI-advised, student-executed | `qpdf --check` passed; 11 pages |

## 4d. Audit table — W5 implementation sprint I check-in (2026-06-09)

| # | Artifact | Tool | Purpose | Prompts / tasks (summary) | Authorship label | Extent of student modification |
|---|---|---|---|---|---|---|
| 33 | `src/safeexec/`, `tests/functional/`, `scripts/smoke_safeexec.py`, `benchmarks/smoke_baseline.py` | Codex (GPT-5, Codex desktop app) | First runnable implementation baseline: models, backend interface, dev subprocess backend, Docker/gVisor command builder, API shell, CLI, smoke script, tests, and benchmark seed | "Use the W5 Canvas assignment and W4 design package to create the smallest credible runnable baseline and smoke evidence" | AI-drafted, student-revised | Student must review every code path, especially the local-backend limitation and Docker/gVisor command controls, before relying on results in the report |
| 34 | `Makefile`, `pyproject.toml`, `requirements.txt`, `deploy/docker-compose.yaml`, `deploy/README.md` | Codex (GPT-5, Codex desktop app) | Reproducible setup/run/test commands and service wrapper for Sprint I | "Add setup/run/test targets and minimal deployment notes without adding unnecessary dependencies" | AI-drafted, student-revised | Student should verify on both local authoring machine and Ubuntu target host as W6 begins |
| 35 | `docs/05-implementation-sprint-i/implementation-sprint-i-check-in.md` | Codex (GPT-5, Codex desktop app) | W5 Canvas-facing check-in narrative with setup, evidence, risks, and forward plan | "Draft the Implementation Sprint I check-in package from actual repo changes and command outputs" | AI-drafted, student-revised | Student should revise into personal voice and confirm Canvas submission contents |
| 36 | `docs/05-implementation-sprint-i/smoke-output.txt`, `test-output.txt`, `benchmark-smoke-output.txt` | Local shell commands advised by Codex | Captured command evidence for smoke execution, unit tests, and benchmark seed | "Run make smoke, make test, and benchmark smoke; save exact outputs" | AI-advised, student-executed | Outputs were generated locally from committed code; student should inspect before submission |
| 37 | `docs/05-implementation-sprint-i/Implementation-Sprint-I-Check-in.docx`, `Implementation-Sprint-I-Check-in.pdf` | `python-docx`, LibreOffice, and render QA | Canvas-ready DOCX/PDF export of the W5 check-in | "Generate DOCX/PDF from the Markdown master and visually verify rendered pages" | AI-advised, student-executed; content authorship per row 35 | Student reviews the final rendered package before Canvas upload |
| 38 | `docs/05-implementation-sprint-i/resubmission-evidence-addendum.md`, `evidence-index.md`, `architecture-notes.md`, `known-issues-risk-log.md`, `CHANGELOG.md`, `canvas-resubmission-checklist.md` | Codex (GPT-5, Codex desktop app) | W5 evidence addendum responding to grading feedback about missing verifiable artifacts | "Map the W5 grading feedback to concrete repository evidence, add missing risk fields, and create a resubmission checklist" | AI-drafted, student-revised | Student should verify the repository URL, commit hash, tag, attachment list, and whether resubmission is allowed |
| 39 | `docs/05-implementation-sprint-i/git-log-w5.txt`, `repository-snapshot.txt`, `smoke-output-2026-06-17.txt`, `test-output-2026-06-17.txt` | Local shell commands advised by Codex | Captured direct evidence for the W5 addendum | "Capture git log, repository file snapshot, fresh smoke output, and fresh test output" | AI-advised, student-executed | Outputs were generated locally from the repository and should be attached if resubmitting |
| 40 | `docs/05-implementation-sprint-i/Implementation-Sprint-I-Evidence-Addendum.docx`, `Implementation-Sprint-I-Evidence-Addendum.pdf` | `python-docx`, LibreOffice, `qpdf`, and render QA | Canvas-ready evidence addendum DOCX/PDF | "Build and visually verify the revised W5 evidence addendum" | AI-advised, student-executed; content authorship per row 38 | Student reviews the final rendered addendum before Canvas upload |

## 4e. Audit table — W6 early implementation validation package (2026-06-17)

| # | Artifact | Tool | Purpose | Prompts / tasks (summary) | Authorship label | Extent of student modification |
|---|---|---|---|---|---|---|
| 41 | `scripts/capture_environment.py`, `scripts/run_validation_workflow.py`, `tests/functional/test_validation_workflow.py`, `Makefile` W6 targets | Codex (GPT-5, Codex desktop app) | Repeatable W6 environment and validation harness for local/API/Docker/gVisor evidence | "Create scripts that capture environment state, run repeatable validation, emit JSON/text evidence, and test the API trace helper" | AI-drafted, student-revised | Student should review validation cases and confirm they match project claims before using in the report |
| 42 | `docs/06-hard-stop-3/evidence*/` | Local shell and SSH commands advised by Codex | Captured local and Ubuntu droplet validation evidence, including first-run Docker image-pull timeout and clean rerun | "Run local validation, clone W6 harness on target host, run Docker/gVisor validation, download evidence outputs" | AI-advised, student-executed | Outputs are generated from actual command runs; student should inspect before submission |
| 43 | `docs/06-hard-stop-3/early-implementation-validation-package.md`, `known-issues-risk-log.md`, `canvas-submission-checklist.md`, DOCX/PDF package | Codex (GPT-5, Codex desktop app) | Hard Stop 3 technical memo and Canvas package | "Interpret W6 validation results honestly, map evidence to assignment rubric, and generate DOCX/PDF with render QA" | AI-drafted, student-revised | Student should verify final wording, limitations, and attachment list before Canvas upload |

## 4f. Audit table — W8 midpoint technical evidence review (2026-06-19)

| # | Artifact | Tool | Purpose | Prompts / tasks (summary) | Authorship label | Extent of student modification |
|---|---|---|---|---|---|---|
| 44 | `scripts/run_midpoint_evidence.py`, `Makefile` W8 targets | Codex (GPT-5, Codex desktop app) | Repeatable midpoint benchmark/evidence harness for correctness, failure-control, and containment-oriented cases across local, Docker, and gVisor backends | "Create a W8 evidence runner that emits JSON/CSV/Markdown summaries and maps evidence to the midpoint technical-review rubric" | AI-drafted, student-revised | Student should review case definitions, expected outputs, and timeout assumptions before using results in final report |
| 45 | `docs/08-hard-stop-4/evidence-local/`, `docs/08-hard-stop-4/evidence-target/` | Local shell and SSH commands advised by Codex | Captured local unit-test/environment evidence and target-host Docker/gVisor midpoint benchmark evidence | "Run local benchmark, copy benchmark script to the Ubuntu target host, run Docker/gVisor benchmark, capture metadata, and download evidence" | AI-advised, student-executed | Outputs were generated from actual command runs; student should inspect raw JSON/CSV and the gVisor timeout before submission |
| 46 | `docs/08-hard-stop-4/midpoint-technical-evidence-review.md`, `known-issues-risk-log.md`, `canvas-submission-checklist.md`, DOCX/PDF package | Codex (GPT-5, Codex desktop app) | Hard Stop 4 technical memo, updated risk log, Canvas checklist, and rendered submission artifacts | "Interpret midpoint evidence, link results to success criteria, document weaknesses, and generate DOCX/PDF with visual QA" | AI-drafted, student-revised | Student should verify final wording, attachment list, and the decision to frame the gVisor timeout as a limitation rather than hide it |

## 4g. Audit table — W10 artifact hardening and reproducibility check (2026-06-26)

| # | Artifact | Tool | Purpose | Prompts / tasks (summary) | Authorship label | Extent of student modification |
|---|---|---|---|---|---|---|
| 47 | `.env.example`, `docs/reproducibility/*.md`, `deploy/README.md`, `README.md`, `Makefile` reproducibility targets | Codex (GPT-5, Codex desktop app) | Harden reviewer setup, configuration transparency, environment notes, data/redistribution policy, artifact manifest, and Make targets | "Use the W10 Canvas assignment to add practical reproducibility docs and setup/run/package commands without broad refactoring" | AI-drafted, student-revised | Student should verify that the setup commands match the environment they want graders to follow |
| 48 | `scripts/audit_reproducibility.py`, `scripts/package_artifact.py`, `docs/10-hard-stop-5/evidence/` | Codex (GPT-5, Codex desktop app) + local shell | Reproducibility audit, source-package builder, command transcripts, clean package run evidence, and environment snapshots | "Create audit/package scripts; run smoke, tests, validation, audit, package export, and clean /tmp unpack run; save outputs" | AI-drafted and AI-advised, student-executed | Outputs were generated from actual commands; student should inspect `clean-run-output.txt` and package contents before submission |
| 49 | `docs/10-hard-stop-5/artifact-hardening-and-reproducibility-check.md`, `known-issues-risk-log.md`, `canvas-submission-checklist.md`, `walkthrough-script.md`, DOCX/PDF package | Codex (GPT-5, Codex desktop app) | Hard Stop 5 technical memo, risk log, Canvas checklist, recording script, and rendered submission artifacts | "Interpret W10 reproducibility results, map them to rubric dimensions, and generate DOCX/PDF with render QA" | AI-drafted, student-revised | Student should verify final wording, attachment list, and walkthrough recording before Canvas upload |

## 4h. Audit table — W12 draft report, deck, and final test evidence (2026-06-26)

| # | Artifact | Tool | Purpose | Prompts / tasks (summary) | Authorship label | Extent of student modification |
|---|---|---|---|---|---|---|
| 50 | `scripts/run_final_evidence.py`, `Makefile` `final-evidence` target, `docs/12-hard-stop-6/evidence/` | Codex (GPT-5, Codex desktop app) + local shell | Fresh W12 evidence bundle runner and command-output evidence for smoke, tests, local validation, reproducibility audit, environment snapshot, and prior W8/W10 evidence references | "Create a repeatable final-evidence command and run it so the W12 package has direct evidence files rather than only prose claims" | AI-drafted and AI-advised, student-executed | Outputs were generated from actual commands; student should inspect the evidence folder before Canvas upload |
| 51 | `docs/12-hard-stop-6/near-final-technical-report-draft.md`, `draft-report-deck-final-test-evidence.md`, `final-test-evidence-appendix.md`, risk log, checklist, README, walkthrough script | Codex (GPT-5, Codex desktop app) | Draft report, Canvas-facing synthesis, evidence appendix, final-readiness risk log, checklist, and recording script for Hard Stop 6 | "Use the W12 Canvas assignment and current repo evidence to align the report, deck, and final-test appendix around one evidence story" | AI-drafted, student-revised | Student should verify final prose, remaining-work statements, and attachment list before submission |
| 52 | `docs/12-hard-stop-6/*.docx`, `*.pdf`, `SafeExec-Draft-Report-and-Demo-Deck.pptx`, `w12-evidence.zip` | Codex (GPT-5, Codex desktop app), python-docx builder, LibreOffice, qpdf, artifact-tool presentation library, render QA | Generated submission artifacts, deck, PDF checks, DOCX page-render QA, slide-preview QA, and zipped evidence folder | "Build and visually verify W12 DOCX/PDF documents and an editable PPTX deck; fix layout issues before delivery" | AI-advised, student-executed; content authorship per rows 50-51 | Student should open the final files and record the walkthrough before Canvas upload |

### Workspace screenshots (`docs/01-launch-packet/screenshots/`)

| # | File | Authorship label | Notes |
|---|---|---|---|
| 16a | `01-repo-folder-structure.png` | Student-only | Captured by student via terminal `tree` command |
| 16b | `02-repo-url.png` | Student-only | Browser screenshot of GitHub repo |
| 16c | `03-issue-tracker.png` | Student-only | Browser screenshot of GitHub Issues tab |
| 16d | `04-ide.png` | Student-only | Screenshot of student's IDE |
| 16e | `05-architecture-rendered.png` | AI-drafted (diagram source), Student-only (export) | Mermaid source is AI-drafted (entry #10); the PNG export was performed by the student via mermaid.live |
| 16f | `06-git-log-initial-commits.png` | Student-only | Terminal screenshot |

## 5. Operational AI use (non-document)

| Date | Tool / channel | Purpose | Authorship label | Outcome |
|---|---|---|---|---|
| 2026-05-13 | Claude (Cowork) advisory chat | Project-topic brainstorm and three-candidate scoping | Student-originated, AI-articulated | Student selected Candidate C |
| 2026-05-13 | Claude (Cowork) via `mcp__workspace__bash` | Local `git init`, configure user, stage W1 artifacts, initial commit `2a280e6` tagged `w1-initial` | AI-advised, student-executed (student reviewed commit message before commit landed) | Initial commit created in student's name |
| 2026-05-13 | Claude (Cowork) + WebSearch + web_fetch | Located 7 bibliography sources from primary documents | AI-advised, student-verified | Student independently re-fetched and read every source |
| 2026-05-14 | Claude (Cowork) via `mcp__workspace__bash` | Second commit (`f2f87bd`) adding git-push instructions and README updates | AI-advised, student-executed | Student reviewed commit |
| 2026-05-14 to 2026-05-17 | Claude (Cowork) advisory chat | DigitalOcean droplet setup choices (region, plan, OS image), Docker + gVisor installation, system-upgrade dialog handling, smoke tests | AI-advised, student-executed | Every command was typed and executed by the student on the droplet; outputs verified by the student |
| 2026-05-17 | Claude (Cowork) advisory chat | Canvas submission package composition | Student-originated, AI-articulated | Student selected attachments and wrote text-entry blurb |
| 2026-05-17 | Claude (Cowork) advisory chat | Discussion-01 peer-discussion pitch and one peer reply | AI-drafted, student-revised | Student reviewed before posting; voice revision applied |
| 2026-05-18 | Claude (Cowork) advisory chat | Response to W1 grading feedback; this log restructuring | AI-drafted, student-revised | This file is the output |
| 2026-05-21 | Claude (Cowork) advisory chat + Read tool on uploaded `02 Proposal Approval Package.pdf` | Read the W2 assignment brief; map its 9 tasks and 6 rubric dimensions to the W1 artifacts that already exist; identify gaps to fill | AI-advised, student-executed | Student selected the four "recommended" options in the clarifying-question round (consolidated DOCX, full script with timing, Gantt+table, fresh formal proposal that supersedes the charter) |
| 2026-05-21 | Claude (Cowork) via Write tool | Draft the five W2 markdown artifacts (proposal, project-plan, wbs, approval-brief, walkthrough-script) | AI-drafted, student-revised | See rows 17–21 in §4a for per-artifact extent of student modification |
| 2026-05-21 | Claude (Cowork) via `mcp__workspace__bash` | Generate consolidated DOCX with `docx-js`; validate; convert to PDF with `soffice` | AI-advised, student-executed | See rows 22–23 in §4a |
| 2026-05-25 | Codex (GPT-5, Codex desktop app) + public web browsing + local shell | Prepare W3 Literature and Requirements Brief; browse public sources; create DOCX builder; export PDF; render PDF pages for QA | AI-drafted, student-revised | See rows 24–27 in §4b |
| 2026-05-27 | Codex (GPT-5, Codex desktop app) + public web browsing | Record student/advisor W3 decisions and make a conservative license/data-reuse call for HumanEval/MBPP subsets | Student-originated, AI-articulated; AI-advised, student-executed | W3 brief, engineering log, and generated DOCX/PDF updated to reflect confirmed decisions |
| 2026-05-28 | Codex (GPT-5, Codex desktop app) | Record W2 proposal approval feedback and update project status markers | AI-advised, student-executed | README, W2 approval brief, and engineering log updated to reflect approval feedback and execution-risk focus |
| 2026-05-30 | Codex (GPT-5, Codex desktop app) + local shell | Prepare W4 Design Review Package; generate diagrams; create DOCX/PDF; render pages for visual QA; update README/logs | AI-drafted, student-revised | See rows 28-32 in §4c |
| 2026-06-09 | Codex (GPT-5, Codex desktop app) + local shell | Prepare W5 Implementation Sprint I baseline; add source/tests/Makefile/deploy notes; run smoke and unit tests; prepare check-in package | AI-drafted, student-revised | See rows 33-37 in §4d |
| 2026-06-17 | Codex (GPT-5, Codex desktop app) + local shell | Respond to W5 grading feedback by preparing a verifiable evidence addendum, enhanced risk log, architecture notes, changelog, and fresh command-output evidence | AI-drafted, student-revised | See rows 38-40 in §4d |
| 2026-06-17 | Codex (GPT-5, Codex desktop app) + local shell + SSH to student-controlled DigitalOcean droplet | Prepare W6 Hard Stop 3 validation package; run local and target-host validation; generate DOCX/PDF; visually QA rendered pages | AI-drafted, student-revised | See rows 41-43 in §4e |
| 2026-06-19 | Codex (GPT-5, Codex desktop app) + local shell + SSH to student-controlled DigitalOcean droplet | Prepare W8 Midpoint Technical Evidence Review; add benchmark harness; run local and target-host evidence; generate DOCX/PDF; visually QA rendered pages | AI-drafted, student-revised | See rows 44-46 in §4f |
| 2026-06-26 | Codex (GPT-5, Codex desktop app) + local shell | Prepare W10 Artifact Hardening and Reproducibility Check; add reproducibility docs/scripts; run local and clean-package evidence; generate DOCX/PDF; visually QA rendered pages | AI-drafted, student-revised | See rows 47-49 in §4g |
| 2026-06-26 | Codex (GPT-5, Codex desktop app) + local shell + artifact-tool presentation library | Prepare W12 Draft Report, Deck, and Final Test Evidence package; add final-evidence runner; run local evidence; draft near-final report and appendix; generate DOCX/PDF/PPTX; visually QA rendered pages and slides | AI-drafted, student-revised | See rows 50-52 in §4h |

## 6. Decisions that were human-only (no AI assistance)

The following analytical and operational decisions involved no AI assistance in any form. They were originated, weighed, and committed to by the student:

- **Choice to pursue a CISC 699 applied project at all**, the course's structural constraints, and the milestone-deadline calendar.
- **Career framing.** The decision to target frontier-AI-lab SWE roles (Anthropic, Google DeepMind) as the project's external-audience anchor.
- **Project topic selection.** The choice to pursue Candidate C (hardened Python execution sandbox) over Candidates A and B was the student's after weighing portfolio fit, risk appetite, and background. AI presented the three options; the student chose one.
- **Scope commitments.** Every in/out-of-scope item that the student approved as a personal commitment: Python-only, no network, no GPU, single-tenant, Linux-only, no production deployment, no multi-tenant security.
- **Resolution of feasibility decisions D1–D6.** All six decisions were resolved by the student personally: HumanEval/MBPP reuse (D1); DigitalOcean as compute provider (D2 — chosen for student credit availability, not AI-suggested as the default); Ubuntu 22.04 (D3); public repository visibility (D4 — chosen against the AI-recommended "private during term"); weekly availability target (D5); supervisor cadence (D6, pending W2 meeting).
- **Supervisor recipient list.** Adding Prof. Lateef alongside Prof. Shaalan on the briefing email was a student decision.
- **All Linux-host commands.** Every command executed on the DigitalOcean droplet was reviewed and executed by the student. No commands were executed by an AI tool on the droplet.
- **All Git commits.** The student reviewed every commit before staging and reviewed every commit message before the commit landed.
- **DigitalOcean specifics.** The droplet's region (NYC3), plan (Premium Intel 2 vCPU / 4 GB / 120 GB NVMe / 4 TB transfer at $32/mo), OS image, and SSH-key setup were student selections informed by AI advice.
- **Workspace screenshots.** All six screenshots were captured by the student.
- **GitHub remote configuration.** Repo name (`liangzixuan/cisc-699`), visibility (public), and any collaborator additions were student-only.
- **Discussion 01 peer-discussion engagement.** The choice to participate, the framing strategy (one strength / one risk / one suggestion), and the post-revision before submission were student decisions.
- **Canvas submission package composition.** The decision to upload PDFs + screenshots + text-entry blurb, the file format for each, and the submission timing (2026-05-17 18:03 ET) were student-only.
- **Acceptance / rejection of every AI recommendation in this project to date.** Where the student deferred to AI advice, this is reflected in the relevant `AI-advised, student-executed` rows. Where the student declined AI advice (e.g., choosing public-from-start visibility against the recommended private default), the decision is recorded as Student-only.

## 7. Ongoing-disclosure process (W2 onward)

The disclosure rigor introduced in W2 will be carried through to W14:

1. **Inline AI-use blocks** at the top of every substantive new artifact (code, docs, figures) added to the repository.
2. **Commit-message tags.** Commits containing AI-assisted content carry an `AI-use:` trailer line naming the tool and the authorship label, e.g.:
   ```
   AI-use: Claude Sonnet 4.6 (Cowork) — AI-drafted, student-revised. Re-wrote evaluation-plan §3 for clarity.
   ```
3. **Code-level annotations.** Code committed to `src/`, `tests/`, or `benchmarks/` carries inline comments tagging substantive AI-drafted blocks, using the conventions `# ai-drafted` (untouched AI output) and `# ai-suggested-then-rewritten` (AI seed, student-finished).
4. **Weekly log update.** This file is updated within 24 hours of any AI-assisted work session. The audit table grows by row per artifact; the operational table grows by row per session.
5. **W14 appendix assembly.** The final-report AI-use appendix is assembled directly from this log: a condensed version of the audit table, the human-only-decisions enumeration, and a session-count summary.
6. **Adversarial-suite caveat.** Per §6 above, the adversarial test suite (the project's central evaluation contribution) is the most important artifact to keep student-authored. Any AI assistance with the adversarial suite will be disclosed at the program level (per individual test program) rather than only at the file level, given the suite's role as the project's intellectual contribution.

## 8. Version history of this log

| Date | Change | Trigger |
|---|---|---|
| 2026-05-13 | Initial creation with W1 description-style entries for the seven launch-packet artifacts. | Project start |
| 2026-05-13 | Added W1 bibliography-drafting entry recording WebSearch + web_fetch usage and per-source verification gaps. | Bibliography draft completed |
| 2026-05-14 | Added W1 entry for the remaining-W1 artifacts (architecture-context, feasibility-memo content, w2-issues, screenshots checklist, git-push instructions, .gitattributes). | W1 artifacts completed |
| 2026-05-18 | Full restructure into audit-oriented format with per-artifact table, decision-authorship taxonomy, human-only-decisions enumeration, ongoing-process section. | W1 grading feedback (Prof. Shaalan, 2026-05-18): "Log appears more descriptive than audit-oriented; in-text attribution is inconsistent; process not systematically documented." |
| 2026-05-21 | Appended §4a (W2 audit rows 17–23) and three rows in §5 (operational AI use); bumped Last-updated to 2026-05-21. | W2 proposal-approval package preparation. |
| 2026-05-25 | Appended §4b (W3 audit rows 24–27) and one row in §5 (operational AI use); bumped Last-updated to 2026-05-25. | W3 literature and requirements brief preparation. |
| 2026-05-27 | Recorded advisor/student W3 decisions and updated the W3 brief package; bumped Last-updated to 2026-05-27. | Advisor review decisions confirmed. |
| 2026-05-28 | Recorded W2 proposal approval feedback and execution-risk follow-up; bumped Last-updated to 2026-05-28. | W2 feedback received. |
| 2026-05-30 | Appended §4c (W4 audit rows 28-32) and one row in §5; bumped Last-updated to 2026-05-30. | W4 design review package preparation. |
| 2026-06-09 | Appended §4d (W5 audit rows 33-37), added the W5 operational-use row, and bumped Last-updated to 2026-06-09. | W5 implementation sprint I baseline and check-in package preparation. |
| 2026-06-17 | Extended §4d with W5 resubmission-evidence rows 38-40 and added a W5 feedback-response operational-use row. | W5 grading feedback response and evidence addendum preparation. |
| 2026-06-17 | Added §4e with W6 validation harness, evidence, package-generation, and operational-use rows 41-43. | Hard Stop 3 early implementation validation package preparation. |
| 2026-06-19 | Added §4f with W8 midpoint benchmark harness, evidence, package-generation, and operational-use rows 44-46; bumped Last-updated. | Hard Stop 4 midpoint technical evidence review preparation. |
| 2026-06-26 | Added §4g with W10 reproducibility docs, audit/package scripts, clean-run evidence, package-generation, and operational-use rows 47-49; bumped Last-updated. | Hard Stop 5 artifact hardening and reproducibility package preparation. |
| 2026-06-26 | Added §4h with W12 final-evidence runner, report/deck/evidence appendix, generated DOCX/PDF/PPTX artifacts, and operational-use rows 50-52. | Hard Stop 6 draft report, deck, and final test evidence package preparation. |
