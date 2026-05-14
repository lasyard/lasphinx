# lasphinx

Common staffs used by sphinx documentation projects.

## Usage

In your project directory:

```sh
git submodule add git@github.com:lasyard/lasphinx.git
```

Then at the beginning of your `conf.py`:

```py
from lasphinx import *
```

Note: the globals in lasphinx must be imported to serve as Sphinx config.

To build html:

```sh
lasphinx/build.sh
```

To clean the build:

```sh
lasphinx/build.sh clean
```

If you are not to use the script for building, in order to find the `lasphinx` module, add the following at the beginning of `conf.py`:

```py
import sys

sys.path.append('.')
```

## Extensions

The module add these extensions to Sphinx:

- `lasyard_literalinclude` is an override of the standard `literalinclude` directive, which have the following features:
  - Automatically set `language` option according to the extension of included file
  - Remove the `---`, `+++` headers if `diff` options is used to hide the file paths which may be sensitive
- `ellipsis_to_vertical` is to replace single lines of `...` to vertical `⋮`s in literal blocks if the language is `console`.

## Styles

CSS files were provided to adjust the appearance of html pages. In the configuration file:

```py
html_static_path = ['lasphinx/static']

if html_theme == 'sphinx_rtd_theme':
    html_css_files = ['lasyard_sphinx_rtd_theme.css']
```

## Scripts

There are scripts to build `drawio` and `puml` files to `png` files, just run in the root of source directory:

Note `drawio` and `plantuml` tools must be installed, and the varible `DRAWIO_CMD` and `PUML_CMD` in file `drawio.mk` and `puml.mk` may need to be changed to the real path of the tools.

The default image source files is searched in directory `_images` and the target images is in `_generated_images`.

## MIT License

<https://lasy.fwh.is/mit_license>
