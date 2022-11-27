#!/usr/bin/env bash

set -euo pipefail

function check_single()
{
    local -r in_path="$1"
    local -i result_val=0
    printf "Checking \"%s\"\n" "${in_path}"
    printf "Checking with pylint:\n"
    if ! poetry run pylint "$in_path" ; then
        result_val=1
    fi

    printf "Checking with flake8:\n"
    local -r flake8_opts="--count --max-line-length=80 --show-source --ignore=E203,W503"
    local -r flake8_cmd="poetry run flake8 $in_path $flake8_opts"
    if ! $flake8_cmd ; then
        result_val=1
    fi
    printf "...done\n\n\n"
    return $result_val
}


declare -i result_code=0

shopt -s globstar
for cur_script in **/*.py;
do
    if ! check_single "$cur_script" ; then
        result_code=1
    fi
done

exit $result_code
