# Gemini Research Harness Template

A Gemini-first, file-based harness for research-heavy work inside a repository.

Use the setup prompt to adapt the template to a real repo. The harness stays local-first, keeps its state in files, and gives Gemini a clear place to put durable research outputs: `research/`.

## Quick Start

1. Copy `GEMINI.md`, `AGENTS.md`, `ARCHITECTURE.md`, `SETUP.md`, `.harness/`, `docs/`, and `research/` into the target repo.
2. Open `SETUP.md`.
3. Paste the prompt into Gemini CLI.
4. Let Gemini rewrite the template so it matches the target repo's real structure, tooling, and research workflow.

## What's Inside

| Path | Purpose |
| --- | --- |
| `GEMINI.md` | Primary Gemini workspace instructions |
| `AGENTS.md` | Minimal compatibility pointer for AGENTS-aware tools |
| `ARCHITECTURE.md` | Stable structure, data flow, and constraints |
| `SETUP.md` | Bootstrap prompt for adapting the template |
| `docs/briefs/` | Research briefs |
| `docs/plans/` | Research plans |
| `.harness/tasks/` | Task packets linking briefs, plans, and outputs |
| `.harness/runs/` | Run records for completed work |
| `research/` | Markdown research notes and final syntheses |

## Research Loop

1. Write a brief in `docs/briefs/`.
2. Write a plan in `docs/plans/`.
3. Create or update a task packet in `.harness/tasks/`.
4. Gather evidence and write the findings to `research/*.md`.
5. Record the result in `.harness/runs/`.

## Design Principles

- Gemini-first: `GEMINI.md` is the instruction entry point.
- Research-first: durable findings belong in `research/`, not chat history.
- File-based: no external services, queues, or hidden orchestration.
- Lean surface: small templates, minimal compatibility files, no helper code.
- Repo-local: adapt the harness to the actual project instead of keeping boilerplate.

## Manual Setup

1. Copy the template into the target repo.
2. Read `GEMINI.md` and `ARCHITECTURE.md`.
3. Paste the prompt from `SETUP.md` into Gemini CLI.
4. After setup, delete `SETUP.md` from the target repo.

## License

MIT
