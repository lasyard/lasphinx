from pathlib import Path

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
    'lasyard_literalinclude',
    'ellipsis_to_vertical',
]

copybutton_prompt_is_regexp = True
copybutton_prompt_text = r"^\$ |^# |^% "

myst_enable_extensions = [
    'attrs_block',
    'attrs_inline',
    'colon_fence',
    'deflist',
    'dollarmath',
    'fieldlist',
    'substitution',
    'tasklist',
]

myst_dmath_allow_labels=True


templates_path = ['_templates']
exclude_patterns = ['.*', '_*', 'Thumbs.db', 'README.*']

lasphinx_dir = Path(__file__).resolve().parent.name

exclude_patterns += [lasphinx_dir]
html_static_path = [f'{lasphinx_dir}/static']
