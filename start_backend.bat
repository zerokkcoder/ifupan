@echo off
echo Starting Backend Server...
cd /d "%~dp0backend"

if not exist "venv" (
    echo Virtual environment not found. Creating one...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo Installing dependencies...
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

echo.
echo Server running at: http://127.0.0.1:8000
echo API Docs at: http://127.0.0.1:8000/docs
echo.

uvicorn app.main:app --reload
pause
