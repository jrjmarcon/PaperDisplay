#!/bin/bash

# Wait for network connection
echo "Checking for internet connection..."
until ping -c1 google.com &>/dev/null; do
  echo "Waiting for network..."
  sleep 2
done
echo "Network is up!"

# navigate to directory of the script
cd "$(dirname "$0")"

# Activate the virtual environment
source ./venv/bin/activate

# Run your script
python3 -u -m scripts.card ## addition after the arrow allows me to log my prints

deactivate