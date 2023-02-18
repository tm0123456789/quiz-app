#!/bin/bash

python3.10 -m venv .venv
source .venv/bin/activate
pip install wheel

if [ "$ENVIRONMENT" == "production" ]
then
  pip install -r requirements.txt
else
  pip install -r requirements-dev.txt
fi