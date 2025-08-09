@echo off
REM Stealth Browser MCP Server - Windows Launcher
REM ==================================================

echo Starting Stealth Browser MCP Server...
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\python.exe" (
    echo ERROR: Virtual environment not found!
    echo Please run: python -m venv venv
    echo Then: venv\Scripts\pip install -r requirements.txt
    pause
    exit /b 1
)

REM Check if requirements are installed
venv\Scripts\python.exe -c "import fastmcp, nodriver" >nul 2>&1
if errorlevel 1 (
    echo WARNING: Dependencies not installed or outdated
    echo Installing/updating dependencies...
    venv\Scripts\pip.exe install -r requirements.txt
)

REM Activate virtual environment and run server
cd /d "%~dp0"
echo Launching MCP server...
venv\Scripts\python.exe src\server.py

echo.
echo Server stopped. Press any key to exit...
pause > nul