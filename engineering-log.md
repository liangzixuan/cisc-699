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
- [x] Complete `supervisor-briefing.md` (decisions still needed from Dr. Shaalan)
- [x] Initialize Git repo and push to private GitHub remote
- [x] Create issue tracker (GitHub Issues) with W2 charter-approval tasks
- [x] Submit launch packet to Canvas
- [x] the supervisor briefing was emailed to Profs. Shaalan and Lateef on the same day

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

*Pending.*

---

## Week 3 (2026-05-23 → 2026-05-29)

*Pending.*
