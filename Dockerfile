# Use Python 3.11 slim image for smaller size
FROM python:3.11-slim

# Install system dependencies including git (needed for py2js installation)
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    xvfb \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome using modern apt method
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/googlechrome-linux-keyring.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/googlechrome-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first for better Docker layer caching
COPY requirements.txt .

# Re-install git temporarily for pip install (needed for git+ dependencies)
RUN apt-get update && apt-get install -y git \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy application code
COPY . .

# Create non-root user for security
RUN useradd -m -u 1000 mcpuser && chown -R mcpuser:mcpuser /app
USER mcpuser

# Expose port (Smithery will set PORT env var)
EXPOSE 8000
ENV PORT=8000

# Health check for FastMCP HTTP server (uses PORT env var)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -s http://localhost:$PORT/mcp -o /dev/null || exit 1

# Start the MCP server - FastMCP auto-detects HTTP mode from PORT env var
CMD ["python", "src/server.py"]