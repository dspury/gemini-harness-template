# Architecture

## Overview
This template is a Gemini-first harness for AI-assisted development. It keeps planning, execution, and review state in repository files and avoids service-side orchestration.

## Core Components

- `GEMINI.md`: Primary Gemini CLI context for this workspace.
- `AGENTS.md`: Compatibility map for Codex-style and other AGENTS-aware tools.
- `docs/briefs/`: Feature briefs that define objective, scope, and acceptance criteria.
- `docs/exec-plans/`: Execution plans that turn a brief into concrete implementation steps.
- `.harness/tasks/`: Task metadata that points at the active brief and plan.
- `.harness/runs/`: Structured run records for implementations and validations.
- `.harness/episodes/`: Compact summaries of completed work and lessons learned.
- `docs/reference/PLATFORM_NOTES.md`: Verified platform-specific guidance for Gemini and Codex usage.
- `src/`: Lightweight harness utilities for logging and validation.
- `tests/`: Unit tests for repo-local utilities.

## Data Flow

1. Define the task in a brief.
2. Create an execution plan.
3. Register the task in `.harness/tasks/`.
4. Implement the change in `src/` and related files.
5. Validate the change with the smallest meaningful local command.
6. Persist the execution result in `.harness/runs/`.
7. Record a short completion summary in `.harness/episodes/`.

## Constraints

- File-based state only.
- Deterministic local behavior.
- No external database, queue, or service dependency for harness tracking.
- Keep root instruction files short; treat `docs/` as the deeper system of record.
- Prefer platform differences in configuration and docs over branching harness code.

## Platform Design

- Gemini strength: hierarchical `GEMINI.md` loading, optional multi-file context via `.gemini/settings.json`, `/memory show`, and skills for on-demand expertise.
- Codex strength: short `AGENTS.md` as a map into a structured docs tree.
- Template rule: support both entry points, but keep the harness artifacts and Python utilities platform-neutral.
