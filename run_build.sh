#!/bin/bash
# Script to emit exit code 10 when rawsource is absent
# For use with git-bisect, to run from sphinx source directory.
# Procedure:
#   git checkout master
#   git bisect start HEAD 1.5.6 --
#   git bisect run ~/tmp/rawsource/run_build.sh
#
# https://github.com/matthew-brett/rawsource has the code at ~/tmp

# Clean, reinstall sphinx
git clean -fxd
pip install -e .
# Run test script, emitting error code 0 (success) or 10 (failure)
MY_DIR=$(dirname "${BASH_SOURCE[0]}")
cd $MY_DIR
rm -rf _build
sphinx-build -b html . _build
