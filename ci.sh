#!/bin/bash

echo "Creating/Starting virtualenv"
if [[ ! -e ./.buzzvenv/bin/activate ]]; then
    virtualenv ./.buzzvenv
fi
source ./.buzzvenv/bin/activate

pip install -r requirements.txt
py.test -s
