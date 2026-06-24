# Conventions for markdown based Sphinx documentation project

- Write docs in MyST Markdown, not reStructuredText
- Use MyST fenced directives such as `:::{toctree}`, `:::{literalinclude}`
- Write admonitions in GitHub style, as quoted block like `> [!NOTE]`, do not nest them
- New content pages typically live beside a section `index.md`
- keep support material in `_files/`, `_images/`, or `_generated_images/` rather than mixing it into navigated content directories
- When showing real configs, manifests, or console captures, prefer `literalinclude` from `_files/...` instead of pasting large inline code blocks
- Use language `console` for embedded console command and output, use `...` lines to abbreviate long terminal output
- Use path written with leading `/` (relative to the docs source root) for image references and `literalinclude` targets
- Section indexes can use `:glob:` if the order of items is not vital
- Section indexes can use `:numbered:` to add sequence numbers to the items
- Follow `.editorconfig`, or:
  - default indentation is 4 spaces
  - JSON/YAML use 2 spaces
  - Markdown keeps trailing whitespace
  - `Makefile`/`.mk` files use tabs
