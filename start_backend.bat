@echo off
echo 正在启动后端服务...
cd /d "%~dp0backend"

if not exist "venv" (
    echo 未找到虚拟环境，正在创建...
    python -m venv venv
    call venv\Scripts\activate.bat
    echo 正在安装依赖...
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

echo.
echo 服务运行地址: http://127.0.0.1:8000
echo API 文档地址: http://127.0.0.1:8000/docs
echo.

python -m app.main
pause
