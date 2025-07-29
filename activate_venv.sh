#!/bin/bash

# Activate virtual environment from main directory
# This script can be run from any subdirectory

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Activate the virtual environment
source "$SCRIPT_DIR/venv/bin/activate"

echo "✅ Virtual environment activated!"
echo "📍 Location: $SCRIPT_DIR/venv"
echo "🐍 Python: $(which python)"
echo "📦 Packages: $(pip list | wc -l) packages installed" 