import sys

from pathlib import Path


lasphinx_dir = Path(__file__).resolve().parent.name
sys.path.append(str(Path(f'{lasphinx_dir}/ext').resolve()))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_rtd_theme',
    'sphinxcontrib.mermaid',
]

extensions += [
    'ellipsis_to_vertical',
    'lasyard_literalinclude',
    'mermaid_fence',
]

copybutton_prompt_is_regexp = True
copybutton_prompt_text = r"^\$ |^# |^% "

myst_enable_extensions = [
    'alert',
    'attrs_block',
    'attrs_inline',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'substitution',
    'tasklist',
]

myst_colon_fence_exact_match=True
myst_dmath_allow_labels=True

templates_path = ['_templates']
exclude_patterns = ['.*', '_*', 'Thumbs.db', 'README.*']

exclude_patterns += [lasphinx_dir]
html_static_path = [f'{lasphinx_dir}/static']

html_css_files = ['lasyard_sphinx_basic.css']

# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html#auto-generated-header-anchors
myst_heading_anchors = 3
