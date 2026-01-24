#!/bin/sh
scriptdir=$(dirname $(realpath "$0"))
cd "$scriptdir/.."
if [ -f ./.venv/bin/activate ]; then source ./.venv/bin/activate; fi
python3 -m pytest system-test -q $*
