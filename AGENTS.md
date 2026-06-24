# Instructions for AI Agents

## Code of conduct

- Do not read/write files in the projects where Agents is not enabled (no `AGENTS.md` in the project root directory)
- Do not read/write files in other projects if you are working in one project, except being told so explicitly
- Do not read/write files that are being ignored by `git`, except being told so explicitly, or try to get my permission
- Refer to file `README.md`/`README.txt` if there is any
- If there are any inconsistencies between this doc and the real project status, stop the current working and request a confirmation; You can go on according the real project status if I confirmed

## High-level architecture

`lasphinx` provides shared Sphinx extensions, styles, and asset-generation scripts for Sphinx based documentation project.

- Dotfiles, underscore-prefixed paths, and `lasphinx` itself are excluded from Sphinx parsing via `exclude_patterns`, so underscore-prefixed directories are support assets rather than standalone documentation trees
