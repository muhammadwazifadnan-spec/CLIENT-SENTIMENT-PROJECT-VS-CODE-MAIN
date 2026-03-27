@echo off
echo =====================================
echo   Starting Sentiment Analysis System
echo =====================================

cd /d %~dp0

REM Activate virtual environment (if you have one)
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate
)

echo Checking if Flask server already running...

REM Kill process using port 5000 (old Flask server)
for /f "tokens=5" %%a in ('netstat -aon ^| find ":5000" ^| find "LISTENING"') do (
    echo Closing old Flask process %%a
    taskkill /F /PID %%a >nul 2>&1
)

echo Starting Flask server...
start /b python app.py

echo Waiting for server to start...
timeout /t 3 >nul

echo Opening browser...
start http://127.0.0.1:5000

echo System started successfully.
pause