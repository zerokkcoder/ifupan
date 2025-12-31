@echo off
echo Starting Frontend Server...
cd /d "%~dp0frontend"

if not exist "node_modules" (
    echo Node modules not found. Installing dependencies...
    call npm install
)

call npm run dev
pause
