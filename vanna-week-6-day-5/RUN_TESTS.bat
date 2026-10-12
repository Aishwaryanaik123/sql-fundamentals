@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Run START.bat first to set up the environment.
  pause
  exit /b 1
)
.venv\Scripts\python.exe test_api.py
pause
