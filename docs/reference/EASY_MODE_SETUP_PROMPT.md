# Easy Mode Setup Prompt

Paste this into Gemini CLI or Codex after copying this template into your target project.

Replace `[PROJECT_NAME]` with your repo name if you want a more specific result.

```text
Set up this repository to use the Gemini Harness Template in a way that fits the existing project instead of blindly copying boilerplate.

Context:
- This repo is the working project: [PROJECT_NAME]
- The harness files from the Gemini Harness Template are already present in the repo
- The goal is to make the harness usable immediately for future tasks

What I want you to do:
1. Read `GEMINI.md`, `AGENTS.md`, `ARCHITECTURE.md`, and `docs/reference/PLATFORM_NOTES.md`.
2. Inspect the current repository structure and identify the real code, docs, and test surfaces.
3. Adapt the harness so it matches this repo's actual structure and workflows.
4. Keep the harness lightweight and file-based. Do not introduce services, databases, or orchestration layers.
5. Preserve existing project conventions. Do not rewrite unrelated docs or rename project files unless necessary.

Set up the harness by doing the following:
- update `GEMINI.md` and `AGENTS.md` so they point at the right project files, test commands, and architecture docs
- update `ARCHITECTURE.md` so it describes this repo's actual structure and where the harness fits
- keep `docs/briefs/`, `docs/exec-plans/`, `.harness/tasks/`, `.harness/runs/`, and `.harness/episodes/`
- create or adjust one example brief, one example execution plan, and one example task packet that are realistic for this repo
- keep the examples narrow and safe
- make sure `.gemini/settings.json` still makes sense for Gemini CLI
- verify the smallest meaningful validation command and name it explicitly

Constraints:
- keep the diff focused
- prefer editing existing harness files over creating lots of new files
- use the standard-library-only harness utilities unless a real project need requires otherwise
- do not claim completion without running at least one real validation command

Deliverables:
- a working harness setup aligned to this repo
- one example task path that demonstrates how to use it
- a short summary of what you changed
- the exact validation command you ran
```

## Notes

- This prompt is meant to bootstrap the harness inside a real project quickly.
- It works best after the template files are already copied into the target repo.
- For Gemini-specific troubleshooting, use `/memory show` to confirm the loaded context files.
