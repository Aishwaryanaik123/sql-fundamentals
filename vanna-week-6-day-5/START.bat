@echo off
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
  echo Python was not found. This package needs Python 3.10 or newer.
  echo Install Python once from https://www.python.org/downloads/ and rerun START.bat.
  pause
  exit /b 1
)
if not exist ".venv\Scripts\python.exe" (
  echo Preparing the environment and downloading required packages...
  py -3 -m venv .venv
  if errorlevel 1 goto failed
  call .venv\Scripts\python.exe -m pip install --upgrade pip
  call .venv\Scripts\python.exe -m pip install -r requirements.txt
  if errorlevel 1 goto failed
)
start "" http://127.0.0.1:8000/docs
.venv\Scripts\python.exe -m uvicorn app:app --host 127.0.0.1 --port 8000
goto end
:failed
echo Setup failed. Check your internet connection and Python installation.
pause
:end
