# Platform Notes

Last verified: 2026-03-14

## Official References

### Gemini CLI
- Project context and hierarchy: <https://geminicli.com/docs/cli/gemini-md/>
- Configuration and `context.fileName`: <https://geminicli.com/docs/reference/configuration/>
- Workspace settings in `.gemini/settings.json`: <https://geminicli.com/docs/cli/settings/>
- Trusted folders behavior: <https://geminicli.com/docs/cli/trusted-folders/>
- Skills and on-demand expertise: <https://geminicli.com/docs/cli/skills/>

### Codex
- Harness guidance and `AGENTS.md` usage: <https://openai.com/index/harness-engineering/>

## Verified Platform Facts

### Gemini CLI
- `GEMINI.md` is the default project context filename.
- Gemini can load one or more alternate context filenames through `context.fileName`.
- Project-level settings live in `.gemini/settings.json`.
- Gemini supports hierarchical context loading, `@path/to/file.md` imports, and `/memory show` for inspecting the effective merged context.
- Gemini supports skills as on-demand expertise instead of forcing all guidance into the always-loaded workspace context.
- If Trusted Folders is enabled and a workspace is untrusted, project settings are ignored until the folder is trusted.

### Codex
- `AGENTS.md` is a standard repo entry point for Codex-oriented harnesses.
- OpenAI's published harness guidance recommends keeping `AGENTS.md` short and using the docs tree as the system of record instead of growing a monolithic instruction file.

## Template Positioning

This template leans into Gemini's strengths by:
- keeping `GEMINI.md` as the primary context file
- shipping `.gemini/settings.json` so Gemini can also load `AGENTS.md`
- keeping the root instructions concise so hierarchical context and skills remain useful
- documenting `/memory show` as the way to verify loaded context

This template leans into Codex-style harness strengths by:
- keeping a short `AGENTS.md` map at the repo root
- treating `docs/` as the durable source of truth
- preserving explicit task, run, and episode artifacts in `.harness/`

## Release Guidance

- Do not duplicate large policy blocks in both `GEMINI.md` and `AGENTS.md`.
- Keep root instruction files short and move deeper operational detail into `docs/`.
- Keep the public docs surface intentionally small; do not add a `docs/generated/` layer unless the generated artifacts are durable and actually worth publishing.
- Treat `.gemini/settings.json` as optional convenience, not the only way the harness works.
- Prefer platform-neutral harness code; reserve platform-specific differences for docs and root instruction files.
- Preserve append-only audit trails in `.harness/runs/` and `.harness/episodes/`; do not design writers that overwrite earlier records with the same base identifier.
