@echo off
setlocal EnableExtensions EnableDelayedExpansion
chcp 65001 >nul

rem ============================================================
rem Urban Development coursework launcher (StarUML 7)
rem Canonical working model: *.mdj
rem ============================================================

set "ROOT=%~dp0"
set "COURSE=%ROOT%urban-development-coursework"
set "STARUML7=C:\Users\User\OneDrive\Desktop\Белов\StarUML7\StarUML\StarUML.exe"

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
echo [2/3] Locating StarUML 7 project...
if not exist "%COURSE%" goto :fail_course

set "MDJ="
set /a MDJ_COUNT=0

for /r "%COURSE%" %%F in (*.mdj) do (
    set /a MDJ_COUNT+=1
    set "MDJ=%%~fF"
)

if !MDJ_COUNT! EQU 0 goto :fail_no_mdj
if !MDJ_COUNT! GTR 1 goto :fail_many_mdj

echo Found:
echo !MDJ!

echo.
echo [3/3] Opening project in StarUML 7...
if not exist "%STARUML7%" goto :fail_staruml

start "" "%STARUML7%" "!MDJ!"
if errorlevel 1 goto :fail_open

echo.
echo ============================================================
echo   DONE
echo   Project: !MDJ!
echo ============================================================
echo.
exit /b 0

:fail_root
echo ERROR: Could not enter repository root:
echo %ROOT%
goto :failed

:fail_git
echo ERROR: git pull failed.
echo Resolve local Git conflicts/network issues and run this file again.
goto :failed

:fail_course
echo ERROR: Coursework folder was not found:
echo %COURSE%
goto :failed

:fail_no_mdj
echo ERROR: No StarUML 7 .mdj project was found inside:
echo %COURSE%
echo.
echo Save the imported project as an .mdj file inside urban-development-coursework
echo and commit/push it to the repository.
goto :failed

:fail_many_mdj
echo ERROR: More than one .mdj project was found inside:
echo %COURSE%
echo.
echo Keep one canonical coursework .mdj file or edit run_coursework.bat
echo to point to the desired file explicitly.
goto :failed

:fail_staruml
echo ERROR: StarUML 7 executable was not found:
echo %STARUML7%
echo.
echo Update STARUML7 in run_coursework.bat if StarUML was moved.
goto :failed

:fail_open
echo ERROR: StarUML 7 could not open:
echo !MDJ!
goto :failed

:failed
echo.
echo ============================================================
echo   FAILED
echo ============================================================
echo.
pause
exit /b 1
