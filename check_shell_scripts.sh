#!/usr/bin/env bash

set -euo pipefail

declare -i result_code=0

shopt -s globstar
for cur_script in **/*.sh;
do
    printf "Checking \"%s\"\n" "${cur_script}"
    if ! shellcheck "$cur_script" ; then
        result_code=1
    fi
done

exit $result_code
