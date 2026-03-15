# Gemini Harness System Instructions

You are operating inside a Gemini-first, file-based harness for structured software work.

## Operating Model
- Follow the task loop: Brief -> Plan -> Task Packet -> Implementation -> Validation -> Run Record -> Episode Record.
- Keep state in repository files. Do not rely on unstated session memory for task tracking.
- Keep changes narrow and deterministic. Avoid broad framework changes unless the task explicitly asks for them.

## Instruction Map
- `README.md`: operator setup and daily workflow
- `ARCHITECTURE.md`: stable repo structure and constraints
- `AGENTS.md`: cross-agent compatibility map
- `docs/reference/PLATFORM_NOTES.md`: verified Gemini and Codex platform differences

## Task Workflow

### 1. Define the task
- Read or create a brief in `docs/briefs/` from `docs/briefs/BRIEF_TEMPLATE.md`.
- Read or create an execution plan in `docs/exec-plans/` from `docs/exec-plans/EXEC_PLAN_TEMPLATE.md`.
- Read or create a task packet in `.harness/tasks/` from `.harness/tasks/TASK_TEMPLATE.json`.

### 2. Implement
- Map only the relevant files.
- Make the smallest viable change in `src/` or the target project surface.
- Do not modify the harness infrastructure unless the task is about the harness itself.

### 3. Validate
- Run the smallest meaningful local test first.
- Default command: `python3 -m unittest discover -s tests -p 'test_*.py'`
- Name the exact validation command before claiming success.

### 4. Record
- After each significant validation attempt, write a run record in `.harness/runs/`.
- When the task is complete and verified, write an episode record in `.harness/episodes/`.

## Gemini-Specific Notes
- `GEMINI.md` is the primary Gemini context file in this template.
- `.gemini/settings.json` also allows Gemini to load `AGENTS.md` for cross-agent compatibility.
- If you need to inspect the effective merged context, use `/memory show`.
- If local context files or settings do not seem active, confirm the workspace trust state in Gemini CLI.
