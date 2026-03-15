# Gemini Harness Template

A structured, file-based harness for executing software tasks with Gemini CLI while remaining legible to AGENTS-based tooling such as Codex-style harnesses.

This template is designed for teams that want:
- explicit task planning artifacts
- local, file-based execution state
- lightweight Python utilities instead of orchestration services
- a Gemini-first setup that still works with `AGENTS.md`-oriented workflows

## What This Template Includes

- `GEMINI.md` as the primary Gemini workspace instruction file
- `AGENTS.md` as a compatibility map for Codex-style and other AGENTS-aware tools
- `docs/briefs/` for task briefs
- `docs/exec-plans/` for execution plans
- `.harness/tasks/` for active task packets
- `.harness/runs/` for run records
- `.harness/episodes/` for completion summaries
- `src/` for small harness utilities
- `tests/` for local validation

## Why This Structure

The template leans into the strengths of each platform:
- Gemini strength: `GEMINI.md`, workspace configuration, hierarchical context, and `/memory show`
- Codex strength: `AGENTS.md` as a short map into a durable docs tree

The harness code stays platform-neutral. Platform-specific behavior lives in the root instruction files and workspace config.

## Setup

1. Copy this folder to your new project location.
2. Ensure Python 3 is installed.
3. Read `GEMINI.md`, `AGENTS.md`, `ARCHITECTURE.md`, and `docs/reference/PLATFORM_NOTES.md`.
4. Run the baseline validation:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

5. If you use Gemini CLI, keep the included workspace settings file at `.gemini/settings.json`. It preserves the official default `GEMINI.md` entry point and also allows Gemini to load `AGENTS.md`.

## Quick Start

1. Copy `docs/briefs/BRIEF_TEMPLATE.md` to a task-specific brief.
2. Copy `docs/exec-plans/EXEC_PLAN_TEMPLATE.md` to a task-specific execution plan.
3. Copy `.harness/tasks/TASK_TEMPLATE.json` to a task-specific packet in `.harness/tasks/`.
4. Ask Gemini to work from that task packet and the referenced brief and plan.
5. Run the smallest meaningful local validation command.
6. Record the validation attempt in `.harness/runs/`.
7. Record task completion in `.harness/episodes/`.

## Official Platform Position

- Official Gemini CLI documentation uses `GEMINI.md` as the default context filename.
- Official Gemini CLI documentation also allows alternate or additional filenames through `context.fileName`, so `AGENTS.md` can be loaded too.
- OpenAI's published Codex harness guidance centers `AGENTS.md` as a short repo map and recommends keeping deeper knowledge in `docs/`.

This template adopts both patterns:
- Gemini-first behavior through `GEMINI.md`
- Codex-friendly compatibility through `AGENTS.md`
- deeper operational detail in `docs/` instead of large root instruction files

## Task Workflow

### 1. Write the brief

Create a file in `docs/briefs/` from `docs/briefs/BRIEF_TEMPLATE.md`.

The brief should define:
- the smallest concrete outcome
- why it matters in this repo
- in-scope work
- out-of-scope work
- acceptance criteria

### 2. Write the execution plan

Create a file in `docs/exec-plans/` from `docs/exec-plans/EXEC_PLAN_TEMPLATE.md`.

The plan should define:
- the implementation approach
- expected files to modify
- validation commands
- risks and mitigations
- completion criteria

### 3. Create the task packet

Create a JSON packet in `.harness/tasks/` from `.harness/tasks/TASK_TEMPLATE.json`.

The packet links the task ID, title, brief, and plan so the task can be picked up reproducibly by an agent or operator.

### 4. Execute the task

Ask Gemini to read:
- `GEMINI.md`
- `AGENTS.md`
- the task packet
- the referenced brief
- the referenced execution plan

Then implement the smallest viable change needed to satisfy the task.

### 5. Validate locally

Start with the smallest meaningful command. For the harness itself, use:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

If your copied project has additional app code, prefer the narrowest repo-defined test command that proves the change.

### 6. Log the run

After a meaningful validation attempt, write a run record:

```bash
python3 -c "from src.run_log_writer import write_run_record; write_run_record({'run_id': 'run-example', 'task_id': 'task-000', 'status': 'passed', 'tests_run': ['python3 -m unittest discover -s tests -p test_*.py'], 'files_changed': ['README.md'], 'summary': 'Release readiness validation'})"
```

### 7. Log completion

When the task is complete and verified, write an episode record:

```bash
python3 -c "from src.episode_log_writer import write_episode_record; write_episode_record({'episode_id': 'episode-example', 'task_id': 'task-000', 'result': 'completed', 'lesson': 'Keep workspace instructions short and move durable detail into docs.'})"
```

## Gemini Notes

- Gemini can inspect the effective merged context with `/memory show`.
- If `AGENTS.md` does not appear in Gemini's effective context, verify that the workspace is trusted and `.gemini/settings.json` is being applied.
- Keep `GEMINI.md` short. Gemini supports hierarchical context loading and imported Markdown, so deeper guidance belongs in `docs/`.

## Repository Layout

```text
.
|-- .gemini/settings.json
|-- .harness/
|   |-- tasks/
|   |-- runs/
|   `-- episodes/
|-- AGENTS.md
|-- ARCHITECTURE.md
|-- GEMINI.md
|-- README.md
|-- docs/
|   |-- briefs/
|   |-- exec-plans/
|   `-- reference/
|-- src/
`-- tests/
```

## Components

- `GEMINI.md`: Gemini-first workspace instructions.
- `AGENTS.md`: compatibility map for AGENTS-aware tools.
- `docs/`: briefs, plans, and reference notes.
- `.harness/`: task metadata, run logs, and episode summaries.
- `src/`: harness utilities such as log writers and validators.
- `tests/`: validation for the harness utilities.

## Philosophy

- File-based: everything important is visible in the repository.
- Deterministic: local utilities use predictable inputs and filenames.
- Auditable: task, run, and episode artifacts make work reviewable.
- Platform-aware: harness code stays neutral, while instruction files and docs lean into each agent platform's strengths.

## Release Notes

- Official source references for Gemini and Codex platform behavior are collected in `docs/reference/PLATFORM_NOTES.md`.
- `.gemini/settings.json` is included as a convenience for Gemini CLI users, but the template still works if a user relies only on `GEMINI.md`.
- The harness utilities use Python standard library modules only.
