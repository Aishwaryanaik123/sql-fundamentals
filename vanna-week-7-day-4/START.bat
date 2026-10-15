@echo off
cd /d "%~dp0"
echo ============================================
echo CIA SQL Analyst - first run setup
echo ============================================
where py >nul 2>nul
if errorlevel 1 (
  echo Python was not found. Install Python 3.10 or newer, then run this file again.
  echo This package cannot run without a Python runtime.
  pause
  exit /b 1
)
if not exist ".venv\Scripts\python.exe" (
  echo Creating local environment and downloading required Python packages...
  py -m venv .venv
  if errorlevel 1 goto error
  .venv\Scripts\python.exe -m pip install --upgrade pip
  .venv\Scripts\python.exe -m pip install -r requirements.txt
  if errorlevel 1 goto error
)
echo Starting API at http://127.0.0.1:8000
echo Interactive API docs: http://127.0.0.1:8000/docs
.venv\Scripts\python.exe -m uvicorn app:app --host 127.0.0.1 --port 8000
pause
:error
echo Setup failed. Check internet connection and Python installation.
pause
