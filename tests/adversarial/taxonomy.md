# Adversarial Suite Taxonomy Seed

> **AI-use disclosure.** Drafted with Codex (GPT-5, Codex desktop app) as a W5
> taxonomy placeholder. AI-drafted, student-revised. Full audit trail:
> `docs/ai-use-log.md`.

The W5 check-in commits the category structure only. Program-level adversarial
tests remain a student-authored W6-W8 deliverable because they are the project's
central evaluation contribution.

| Category | Planned probe family | Expected contained outcome |
|---|---|---|
| Resource exhaustion | CPU spin, memory pressure, output flood | Timeout, memory failure, or output truncation without host impact |
| Filesystem boundary | Attempts to inspect host paths or persist files | Denied path, empty view, or ephemeral cleanup |
| Network egress | Attempts to open outbound sockets | Connection failure or timeout |
| Process boundary | Fork/process count pressure | PID-limit failure or timeout |
| Privilege/capability | UID, capability, mount, and namespace probes | Non-root/no-capability evidence |
| Runtime leakage | `/proc`, file descriptor, environment probes | No host-sensitive leakage |
