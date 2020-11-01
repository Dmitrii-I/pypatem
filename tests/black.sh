#!/usr/bin/env bash

POSIXLY_CORRECT=1 set -o errexit && set -o nounset && set -o pipefail && unset POSIXLY_CORRECT

# This script uses relative paths. To avoid errors, make sure this script's
# working directory is the project's root.
cd "$(dirname $0)" && cd ../ && test -f .project-root-dir

source .venv/bin/activate

black --verbose --check --line-length 120 -v src/
black --verbose --check --line-length 120 -v tests/
