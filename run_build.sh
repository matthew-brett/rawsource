#!/bin/bash
git clean -fxd
pip install -e .
MY_DIR=$(dirname "${BASH_SOURCE[0]}")
cd $MY_DIR
rm -rf _build
sphinx-build -b html . _build
