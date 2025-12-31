Write-Host "正在启动后端服务..."
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location "$scriptPath\backend"

if (-not (Test-Path "venv")) {
    Write-Host "未找到虚拟环境，正在创建..."
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    Write-Host "正在安装依赖..."
    pip install -r requirements.txt
} else {
    .\venv\Scripts\Activate.ps1
}

Write-Host ""
Write-Host "服务运行地址: http://127.0.0.1:8000"
Write-Host "API 文档地址: http://127.0.0.1:8000/docs"
Write-Host ""

python -m app.main
Read-Host -Prompt "按回车键退出"
