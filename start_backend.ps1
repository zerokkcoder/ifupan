Write-Host "Starting Backend Server..." -ForegroundColor Green

$ScriptPath = $PSScriptRoot
$BackendPath = Join-Path $ScriptPath "backend"
Set-Location $BackendPath

if (-not (Test-Path "venv")) {
    Write-Host "Virtual environment not found. Creating one..." -ForegroundColor Yellow
    python -m venv venv
    
    # Activate and install
    & ".\venv\Scripts\python.exe" -m pip install -r requirements.txt
}

Write-Host "Server running at: http://127.0.0.1:8000" -ForegroundColor Cyan
Write-Host "API Docs at: http://127.0.0.1:8000/docs" -ForegroundColor Cyan
Write-Host ""

# Use the python executable from venv directly to ensure correct environment
& ".\venv\Scripts\python.exe" -m uvicorn app.main:app --reload
