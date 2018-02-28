#!/bin/bash

cmd="${1:-run}"
if [ "$cmd" == "test" ]; then
    pytest slackbucket/tests
elif [ "$cmd" == "run" ]; then
    python bucket.py
fi
