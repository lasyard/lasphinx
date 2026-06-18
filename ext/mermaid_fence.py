import re


MERMAID_FENCE_RE = re.compile(r"(^|\n)(?P<indent>[ \t]*)```mermaid\n", re.IGNORECASE)


def rewrite_github_mermaid_fence(app, docname, source):
    text = source[0]
    rewritten = MERMAID_FENCE_RE.sub(r"\1\g<indent>```{mermaid}\n", text)
    if rewritten != text:
        source[0] = rewritten


def setup(app):
    app.connect("source-read", rewrite_github_mermaid_fence)
    return {
        "version": "1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
