@echo off
echo Starting Netflix Data Visualization Analysis...
echo.

REM Try different Python commands
python run_analysis.py 2>nul
if %errorlevel% equ 0 goto success

py run_analysis.py 2>nul
if %errorlevel% equ 0 goto success

python3 run_analysis.py 2>nul
if %errorlevel% equ 0 goto success

echo Python not found! Please install Python first.
echo You can download Python from: https://www.python.org/downloads/
pause
exit /b 1

:success
echo.
echo Analysis completed successfully!
echo Check 'netflix_analysis.png' for the visualization.
pause
