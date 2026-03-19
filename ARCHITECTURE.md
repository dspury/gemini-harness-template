# Architecture

## Overview

This template is a Gemini-first research harness. It keeps briefs, plans, research notes, and run records in the repository so work stays local, durable, and easy to audit.

## Structure

```text
.
├── GEMINI.md              # Primary Gemini instruction surface
├── AGENTS.md              # Minimal compatibility pointer
├── ARCHITECTURE.md        # Structure, data flow, and constraints
├── SETUP.md               # Bootstrap prompt for adapting the template
├── .harness/
│   ├── tasks/             # Task packets linking briefs, plans, and outputs
│   └── runs/              # Run records for completed research or implementation work
├── docs/
│   ├── briefs/            # Research briefs: what to answer and why
│   └── plans/             # Research plans: how to answer it
└── research/              # Durable Markdown findings and syntheses
```

## Data Flow

1. Define the question in a brief.
2. Write a plan for how the research will be done.
3. Create or update a task packet when structured tracking is useful.
4. Gather evidence from repo-local material and approved outside sources.
5. Write the findings to `research/*.md`.
6. Record the result in `.harness/runs/`.

## Constraints

- File-based state only.
- Gemini-first instruction surface.
- Markdown for human-authored briefs, plans, and research notes.
- JSON for task packets and run records.
- No helper code, services, queues, or hidden orchestration.
- Keep root files short and move durable outputs into `research/`.
