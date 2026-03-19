# Gemini Research Harness

You are operating inside a Gemini-first, research-oriented harness.

## Operating Model

- Use `GEMINI.md` as the primary instruction surface.
- Read `ARCHITECTURE.md` before changing the harness structure.
- Keep work local, file-based, and easy to audit.
- Store durable research findings in `research/*.md`, not only in chat.
- Keep scope narrow and prefer small, observable changes.

## Workflow

1. Read or create a brief in `docs/briefs/`.
2. Read or create a plan in `docs/plans/`.
3. Create or update a task packet in `.harness/tasks/` when the work needs structured tracking.
4. Gather evidence from the repo and approved external sources.
5. Write the findings, citations, open questions, and recommendations to `research/*.md`.
6. Record the run in `.harness/runs/`.

## Research Rules

- Prefer one research question or topic per Markdown file.
- Name files so they sort cleanly, for example `YYYY-MM-DD-topic.md`.
- Separate evidence from inference.
- Cite sources clearly enough that another agent can verify them.
- If the answer is uncertain, say what is unknown and what would resolve it.

## Validation

- Run the smallest meaningful validation for the change.
- Name the exact command or inspection used before claiming completion.
- If no executable validation exists, say that directly and state what was reviewed instead.
