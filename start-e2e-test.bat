@echo off
chcp 65001 >nul
python -u "%~dp0run_server.py"
pause
