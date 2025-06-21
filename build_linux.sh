#!/bin/bash

# Check if pyinstaller exists
if ! command -v pyinstaller &> /dev/null
then
  echo "Error: pyinstaller not found. Please install it using pip install pyinstaller" &> /dev/stderr
  exit 1
fi

# Create the executable using pyinstaller
pyinstaller --onefile main.py

echo "Executable created in dist/main"
