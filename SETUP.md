# Gemini Research Harness Setup

Paste the prompt below into Gemini CLI after copying this template into the target repository.

Replace `[REPO_NAME]` with the real repository name.

```text
Set up the Gemini research harness in this repository so it matches the real project instead of staying generic boilerplate.

Context:
- This repo is: [REPO_NAME]
- The harness files are already present
- `GEMINI.md` is the primary instruction file
- The goal is a lean, repo-specific research harness

Steps:
1. Read `GEMINI.md` and `ARCHITECTURE.md`.
2. Inspect the repository and identify the real code, docs, and validation surfaces.
3. Rewrite `GEMINI.md` so it points to the real project structure and research workflow.
4. Rewrite `ARCHITECTURE.md` so it reflects the actual repo layout.
5. Update `README.md` so a human can understand how to use the harness.
6. Keep `AGENTS.md` minimal and compatibility-only.
7. Create or adapt one realistic brief in `docs/briefs/`, one plan in `docs/plans/`, one task packet in `.harness/tasks/`, and one research note in `research/`.
8. Keep the harness file-based and local-first. Do not add services, databases, or orchestration.
9. Run one real validation command from the repo and name it explicitly.
10. Delete `SETUP.md` after setup is complete.

Constraints:
- Keep the diff focused.
- Prefer editing existing harness files over adding new layers.
- Use `research/` for durable findings instead of burying them in root docs.
- Do not claim completion without running a real validation command.

Deliverables:
- A repo-specific Gemini research harness
- One example research workflow path
- The exact validation command that was run
- A short summary of what changed
```
