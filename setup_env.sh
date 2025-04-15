#!/bin/bash
# Setup environment for the project

# Exit on error
set -e

# Print commands
set -x

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Create directories if they don't exist
echo "Creating directories..."
mkdir -p assets
mkdir -p notebooks

# Convert Excel files to CSV if they exist
echo "Converting Excel files to CSV..."
if [ -f "convert_xlsx_to_csv.py" ]; then
    python convert_xlsx_to_csv.py assets
fi

# Print success message
echo "Environment setup complete!"
echo "To activate the virtual environment, run: source venv/bin/activate"
