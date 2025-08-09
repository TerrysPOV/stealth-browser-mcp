#!/bin/bash
# Stealth Browser MCP Server - Linux/macOS Launcher
# ===================================================

echo "Starting Stealth Browser MCP Server..."
echo

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if virtual environment exists
if [ ! -f "venv/bin/python" ]; then
    echo "ERROR: Virtual environment not found!"
    echo "Please run: python -m venv venv"
    echo "Then: venv/bin/pip install -r requirements.txt"
    exit 1
fi

# Check if requirements are installed
if ! venv/bin/python -c "import fastmcp, nodriver" 2>/dev/null; then
    echo "WARNING: Dependencies not installed or outdated"
    echo "Installing/updating dependencies..."
    venv/bin/pip install -r requirements.txt
fi

# Run the server
echo "Launching MCP server..."
venv/bin/python src/server.py

echo
echo "Server stopped."