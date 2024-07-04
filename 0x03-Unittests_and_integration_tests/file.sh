#!/bin/bash

# Make all Python files executable
chmod u+x *.py

# Define a list of files to exclude
EXCLUDE_FILES='main.py|utils.py|fixtures.py|client.py'

# Run black on all Python files, excluding specified files
black $(ls *.py | grep -v -E "$EXCLUDE_FILES")

# Run pycodestyle on all Python files, excluding specified files
pycodestyle $(ls *.py | grep -v -E "$EXCLUDE_FILES")

