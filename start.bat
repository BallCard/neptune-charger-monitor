@echo off
chcp 65001 >nul
cd /d "%~dp0"

where python >nul 2>nul
if errorlevel 1 (
    echo [错误] 未检测到 Python，请先安装 Python 3.8+ 并勾选“加入 PATH”。
    pause
    exit /b 1
)

echo 正在启动监控面板，浏览器将自动打开 http://127.0.0.1:8000
start "" powershell -NoProfile -Command "Start-Sleep -Seconds 2; Start-Process 'http://127.0.0.1:8000'"
python monitor.py
