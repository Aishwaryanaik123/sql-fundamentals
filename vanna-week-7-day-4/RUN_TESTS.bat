@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Run START.bat once first so dependencies are prepared.
  pause
  exit /b 1
)
.venv\Scripts\python.exe -m pytest -q
pause
