#!/bin/bash
set -e

# Set up Chrome flags for containerized environment
export CHROME_BIN=/usr/bin/google-chrome-stable
export CHROME_PATH=/usr/bin/google-chrome-stable

# Additional Chrome flags for Render environment
export CHROME_FLAGS="--no-sandbox --disable-dev-shm-usage --disable-gpu --disable-software-rasterizer --remote-debugging-port=9222"

# Set working directory
cd /app

# Start the MCP server with HTTP transport
python src/server.py --transport http --host 0.0.0.0 --port ${PORT:-8000}