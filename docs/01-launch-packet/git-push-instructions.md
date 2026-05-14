# Push Local Repository to GitHub

> The local Git repository was initialized and the W1 launch packet was committed as `2a280e6` and tagged `w1-initial`. This file is the 5-minute procedure for pushing it to a private GitHub remote, which is what the rubric "professional process" dimension expects to see.

## Option A — GitHub CLI (fastest, recommended)

If you have the `gh` CLI installed (`brew install gh && gh auth login`):

```bash
cd ~/PycharmProjects/CISC-699
gh repo create cisc-699-safeexec --private --source=. --push --description "CISC 699 applied project — hardened Python execution sandbox for LLM agent tool-use"
```

That's it — the repo is created on GitHub, the remote is added, and `git push` runs automatically.

Then add the supervisor as a collaborator:

```bash
gh repo edit --add-collaborator <supervisor-github-handle>
# or via the web UI: Settings → Collaborators → Add people
```

## Option B — Web UI + manual remote

1. Go to [github.com/new](https://github.com/new).
2. Repository name: `cisc-699-safeexec` (or whatever you like — keep it lowercase, no spaces).
3. Visibility: **Private** (per feasibility-memo D4).
4. Do **not** initialize with a README, .gitignore, or license — you already have those.
5. Click "Create repository."
6. Copy the SSH URL it shows (looks like `git@github.com:<your-username>/cisc-699-safeexec.git`).
7. Run:

```bash
cd ~/PycharmProjects/CISC-699
git remote add origin git@github.com:<your-username>/cisc-699-safeexec.git
git push -u origin main
git push --tags
```

8. Web UI → Settings → Collaborators → invite supervisor.

## Verify it worked

- Visit the repo URL in a browser.
- Confirm the README renders with the project overview at the top.
- Open `docs/01-launch-packet/architecture-context.md` in the browser — the Mermaid diagram should render natively.
- Open Issues tab — currently empty (next: see `w2-github-issues.md`).

## Next: populate the issue tracker

After the push, create the W1/W2 issues from `w2-github-issues.md`. Either copy-paste 8 issues manually (≈10 minutes) or, if you have `gh` installed, automate it:

```bash
# Example for one issue; repeat per block in w2-github-issues.md
gh issue create \
  --title "Revise project charter into own voice" \
  --label "w1,charter" \
  --body "$(sed -n '/^### Issue 1/,/^### Issue 2/p' docs/01-launch-packet/w2-github-issues.md)"
```

(Or do it in 10 minutes via the web UI — it's a one-time job.)

## Commit hygiene going forward

- One logical change per commit.
- Imperative-mood commit subjects: "Add Docker baseline executor" not "Added Docker baseline executor" or "Adding...".
- Body wrapped at 72 columns when needed for context.
- Reference issues by number: "Closes #14" closes the issue when the PR merges.
- Tag major milestones: `w2-charter-approved`, `w5-hello-world`, `w7-midpoint`, `w11-draft`, `w14-final`.
