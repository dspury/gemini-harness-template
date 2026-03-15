# Repo AGENTS.md

## Purpose
This repository is a Gemini-first harness template that also stays legible to tools that look for `AGENTS.md`.

## Instruction Surface
- `GEMINI.md` is the primary Gemini CLI context file.
- `AGENTS.md` is a compatibility map for Codex and other agent tooling.
- `ARCHITECTURE.md` defines the stable repo structure and constraints.
- `docs/reference/PLATFORM_NOTES.md` explains the verified Gemini and Codex platform differences behind this template.

## Working Rules
- keep the harness file-based and local-first
- keep root instruction files short and use `docs/` as the system of record
- prefer deterministic artifacts over hidden state
- keep task metadata in `.harness/tasks/`
- keep run records in `.harness/runs/`
- keep episode summaries in `.harness/episodes/`
- update docs when workflow or platform assumptions change

## Gemini Notes
- Gemini CLI defaults to loading `GEMINI.md`
- this template also ships `.gemini/settings.json` so Gemini can load `AGENTS.md` alongside `GEMINI.md`
- if Trusted Folders is enabled and the workspace is untrusted, local `.gemini/settings.json` is ignored until the folder is trusted
- use `/memory show` inside Gemini CLI to confirm the effective context

## Validation
- run `python3 -m unittest discover -s tests -p 'test_*.py'`
- do not claim the harness is ready without naming the exact command run
