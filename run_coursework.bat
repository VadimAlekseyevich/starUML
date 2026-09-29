@echo off
setlocal EnableExtensions
chcp 65001 >nul

rem ============================================================
rem Urban Development coursework launcher (Windows / StarUML 7)
rem Pull changes, then open the single canonical MDJ in repo root.
rem To override the executable path, set STARUML7 before running.
rem ============================================================

set "ROOT=%~dp0"
set "MDJ=%ROOT%urban_development_functionality.mdj"

if not defined STARUML7 set "STARUML7=C:\Users\User\OneDrive\Desktop\Белов\StarUML7\StarUML\StarUML.exe"

echo.
echo ============================================================
echo   Urban Development Coursework - StarUML 7
echo ============================================================
echo.

cd /d "%ROOT%"
if errorlevel 1 goto :fail_root

echo [1/3] Pulling latest changes...
git pull --ff-only
if errorlevel 1 goto :fail_git

echo.
echo [2/3] Checking coursework project...
if not exist "%MDJ%" goto :fail_mdj
echo Found: "%MDJ%"

echo.
echo [3/3] Opening project in StarUML 7...
if not exist "%STARUML7%" if exist "%ProgramFiles%\StarUML\StarUML.exe" set "STARUML7=%ProgramFiles%\StarUML\StarUML.exe"
if not exist "%STARUML7%" if exist "%LOCALAPPDATA%\Programs\StarUML\StarUML.exe" set "STARUML7=%LOCALAPPDATA%\Programs\StarUML\StarUML.exe"
if not exist "%STARUML7%" goto :fail_staruml

start "" "%STARUML7%" "%MDJ%"
if errorlevel 1 goto :fail_open

echo.
echo DONE. Project: "%MDJ%"
exit /b 0

:fail_root
echo ERROR: Could not enter repository root: "%ROOT%"
goto :failed

:fail_git
echo ERROR: git pull --ff-only failed.
echo Resolve network issues or local Git changes, then retry.
goto :failed

:fail_mdj
echo ERROR: Coursework project not found: "%MDJ%"
goto :failed

:fail_staruml
echo ERROR: StarUML 7 executable not found.
echo Checked: "%STARUML7%"
echo Set STARUML7 to the full path of StarUML.exe if it is installed elsewhere.
goto :failed

:fail_open
echo ERROR: Could not start StarUML 7.
goto :failed

:failed
echo.
echo FAILED.
pause
exit /b 1
