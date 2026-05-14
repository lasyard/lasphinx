#!/usr/bin/env sh

if ! command -v sphinx-build >/dev/null 2>&1; then
    echo "sphinx-build not found, activating virtualenv if available"
    if ! ${VIRTUAL_ENV:-false}; then
        echo "Not in a virtualenv, attempting to activate .venv, ~/.venv"
        if [ -f .venv/bin/activate ]; then
            . ./.venv/bin/activate
        elif [ -f ~/.venv/bin/activate ]; then
            . ~/.venv/bin/activate
        fi
    fi
fi

SCRIPT_DIR="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
LASPHINX_DIR="${SCRIPT_DIR##*/}"

case $1 in
clean)
    PYTHONPATH=. make clean
    make -f ${LASPHINX_DIR}/scripts/images.mk clean
    ;;
*)
    make -f ${LASPHINX_DIR}/scripts/images.mk
    PYTHONPATH=. make html
    ;;
esac
