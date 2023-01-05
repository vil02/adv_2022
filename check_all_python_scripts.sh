#!/usr/bin/env bash

set -euo pipefail

find . -name "*.py" -not -path "./tests/example_data/python3/*" -exec ./check_python_file.sh {} +
