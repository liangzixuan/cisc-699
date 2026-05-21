# Workspace Screenshots Checklist

> **AI-use disclosure.** Drafted with Claude Sonnet 4.6 (Cowork desktop app). AI-drafted (this checklist), Student-only (the screenshots themselves). The actual workspace screenshots in `screenshots/` were captured by Zixuan Liang — they are the only artifacts in the launch packet that involved no AI assistance in their content. Full audit trail: [`docs/ai-use-log.md`](../ai-use-log.md).

**Purpose.** The launch packet's "Tools" table requires a "screenshot of environment, repository URL or screenshot, folder structure, and basic environment inventory" as W1 evidence. The "Extras to Help the Student Finish Properly" section names "workspace screenshots" as one of the five items in the suggested submission package. This file lists exactly which screenshots to capture and where to save them.

**Where to save:** `docs/01-launch-packet/screenshots/` (create this folder before capturing). PNG format, downsized to ≤500 KB per file before committing. Reference in `README.md` and link in the Canvas submission.

**Naming convention:** `NN-short-description.png` (e.g., `01-repo-folder-structure.png`). The numeric prefix makes ordering stable.

---

## Required screenshots (5)

### 01 — Repo folder structure
**Capture:** Terminal or file-manager view showing the top-level repository layout. The `tree` command output is preferred for clarity:
```
tree -L 2 -I '.git|.idea|__pycache__|.venv' .
```
Or, on macOS without `tree`: `find . -maxdepth 2 -not -path '*/\.*' | sort`.

**What this proves:** Process discipline — the launch packet expects organized scaffolding before any code is written.

---

### 02 — Repository URL (GitHub remote)
**Capture:** Browser screenshot of the private GitHub repository page, showing:
- Repo name and "Private" badge
- The README rendered (top of page)
- File tree visible
- At least one commit in the history

**What this proves:** Version control is set up, not just discussed. The packet's grading rubric weights "professional process" and a real GitHub repo is the most legible evidence.

---

### 03 — Issue tracker populated
**Capture:** GitHub Issues tab showing the W1/W2 issues from `w2-github-issues.md` already created, with labels visible.

**What this proves:** The "issue tracker" item in the launch packet's task list is operational, not just nominally created.

---

### 04 — IDE / development environment
**Capture:** Your IDE (PyCharm, VS Code, etc.) with the project open, README visible in one pane and the project tree in the sidebar.

**What this proves:** A working dev environment exists. Implicit signal of seriousness.

---

### 05 — Mermaid diagram rendered
**Capture:** Either the architecture diagram rendered on GitHub (open `docs/01-launch-packet/architecture-context.md` in the browser on github.com — Mermaid renders natively) or the exported SVG/PNG from mermaid.live.

**What this proves:** The W1 architecture/context-diagram deliverable is real and reviewable, not just a Markdown code block the grader has to imagine.

---

## Optional screenshots (recommended but not required)

### 06 — Terminal showing `git log --oneline` of initial commits
Optional but adds depth — shows that commit hygiene started from day one, not just on submission day.

### 07 — `docker --version && runsc --version` output
Only if these are already installed at W1. More appropriate as W2 evidence.

---

## After capturing — update the README

Append a section to `README.md`:

```markdown
## Workspace evidence

See `docs/01-launch-packet/screenshots/` for W1 workspace screenshots.

- [Repo folder structure](docs/01-launch-packet/screenshots/01-repo-folder-structure.png)
- [GitHub repository view](docs/01-launch-packet/screenshots/02-repo-url.png)
- [Issue tracker](docs/01-launch-packet/screenshots/03-issue-tracker.png)
- [Development environment](docs/01-launch-packet/screenshots/04-ide.png)
- [Architecture diagram (rendered)](docs/01-launch-packet/screenshots/05-architecture-rendered.png)
```

---

## Quick rationale

These five screenshots collectively cover the launch packet's stated evidence requirements:

| Requirement (packet's wording) | Covered by |
|---|---|
| "Screenshot of environment" | #04 |
| "Repository URL or screenshot" | #02 |
| "Folder structure" | #01 |
| "Basic environment inventory" | #04 + #06 (optional) |
| "Architecture/context diagram evidence" | #05 |
| "Issue board" | #03 |
