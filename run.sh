#!/bin/bash


# navigate to directory of the script
cd "$(dirname "$0")"

# Activate the virtual environment
source ./venv/bin/activate

# Run your script
python3 -m scripts.card

deactivate