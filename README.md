# Gemini Harness Template

A Gemini-first, file-based harness for structured software work.

It keeps task definition, execution, validation, and review state in the repository instead of hidden agent memory or external services. The template also stays compatible with `AGENTS.md`-oriented tooling such as Codex-style harnesses.

## Easy Mode

If you want the fastest path, do this:

1. Copy this template into your working project.
2. Open [`docs/reference/EASY_MODE_SETUP_PROMPT.md`](docs/reference/EASY_MODE_SETUP_PROMPT.md).
3. Paste the prompt into Gemini or Codex.
4. Let the agent adapt the harness to your real repo structure, test commands, and docs.

This is the intended quick-start path for most people. The manual startup procedure is still documented below when you want tighter control.

## What You Get

- `GEMINI.md` as the primary Gemini workspace instruction file
- `AGENTS.md` as a compatibility map for AGENTS-aware tools
- `docs/briefs/` for task briefs
- `docs/exec-plans/` for execution plans
- `.harness/tasks/` for active task packets
- `.harness/runs/` for run records
- `.harness/episodes/` for completion summaries
- `src/` for small harness utilities
- `tests/` for local validation
- `LICENSE` with MIT terms

## Manual Setup

1. Copy this folder to your new project location.
2. Ensure Python 3 is installed.
3. Read `GEMINI.md`, `AGENTS.md`, `ARCHITECTURE.md`, and `docs/reference/PLATFORM_NOTES.md`.
4. Run the baseline validation:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

5. If you use Gemini CLI, keep `.gemini/settings.json` in place. It preserves the official `GEMINI.md` entry point and also allows Gemini to load `AGENTS.md`.

## Task Loop

### 1. Create the brief

Copy `docs/briefs/BRIEF_TEMPLATE.md` to a task-specific brief.

The brief should capture:
- the target outcome
- why it matters
- scope and non-scope
- acceptance criteria

### 2. Create the execution plan

Copy `docs/exec-plans/EXEC_PLAN_TEMPLATE.md` to a task-specific plan.

The plan should capture:
- the implementation approach
- likely files to change
- validation commands
- key risks
- completion criteria

### 3. Create the task packet

Copy `.harness/tasks/TASK_TEMPLATE.json` to a task-specific packet in `.harness/tasks/`.

The packet ties together the task ID, brief, and plan so the work can be picked up reproducibly.

### 4. Execute the task

Ask Gemini to read:
- `GEMINI.md`
- `AGENTS.md`
- the task packet
- the referenced brief
- the referenced plan

Then implement the smallest viable change that satisfies the task.

### 5. Validate locally

Start with the smallest meaningful command. For the harness itself, use:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

If you copy this template into a larger project, prefer the narrowest repo-defined command that proves the change.

### 6. Record the run

After a meaningful validation attempt, write a run record:

```bash
python3 -c "from src.run_log_writer import write_run_record; write_run_record({'run_id': 'run-example', 'task_id': 'task-000', 'status': 'passed', 'tests_run': ['python3 -m unittest discover -s tests -p test_*.py'], 'files_changed': ['README.md'], 'summary': 'Release readiness validation'})"
```

Run records are append-safe. If `run-task-000.json` already exists, the writer creates `run-task-000-2.json`, `run-task-000-3.json`, and so on.

### 7. Record completion

When the task is complete and verified, write an episode record:

```bash
python3 -c "from src.episode_log_writer import write_episode_record; write_episode_record({'episode_id': 'episode-example', 'task_id': 'task-000', 'result': 'completed', 'lesson': 'Keep workspace instructions short and move durable detail into docs.'})"
```

Episode records use the same append-safe naming rule.

## Key Files

- `GEMINI.md`: Gemini-first workspace instructions
- `AGENTS.md`: compatibility map for AGENTS-aware tools
- `ARCHITECTURE.md`: stable repo structure and constraints
- `docs/reference/EASY_MODE_SETUP_PROMPT.md`: copy-paste setup prompt for adapting the harness inside a real repo
- `docs/reference/PLATFORM_NOTES.md`: verified Gemini and Codex platform notes
- `.gemini/settings.json`: Gemini workspace configuration

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
|-- LICENSE
|-- docs/
|   |-- briefs/
|   |-- exec-plans/
|   `-- reference/
|-- src/
`-- tests/
```

## Platform Notes

- Gemini CLI officially uses `GEMINI.md` as the default context filename.
- Gemini CLI can also load alternate or additional filenames through `context.fileName`, which is why this template carries `AGENTS.md` too.
- OpenAI's published Codex harness guidance uses `AGENTS.md` as a short repo map and pushes deeper operational detail into `docs/`.

This template follows that split:
- Gemini-first behavior through `GEMINI.md`
- Codex-friendly compatibility through `AGENTS.md`
- durable detail in `docs/` instead of large root instruction files

## Gemini Tips

- Use `/memory show` to inspect Gemini's effective merged context.
- If `AGENTS.md` does not appear in Gemini's context, confirm the workspace is trusted and `.gemini/settings.json` is being applied.
- Keep `GEMINI.md` short. Use `docs/` for durable detail.

## Release Notes

- The harness utilities use Python standard library modules only.
- The project is released under the MIT License.
