@echo off
setlocal EnableExtensions
chcp 65001 >nul

rem ============================================================
rem Urban Development coursework launcher
rem 1) Pull latest changes
rem 2) Build StarUML project
rem 3) Validate model
rem 4) Run methodology audit
rem 5) Open generated .uml in StarUML
rem ============================================================

set "ROOT=%~dp0"
set "COURSE=%ROOT%urban-development-coursework"
set "UML=%COURSE%\dist\urban_development.uml"
set "REGISTRY=%COURSE%\model\registry.json"
set "TRACE=%COURSE%\model\traceability.json"

echo.
echo ============================================================
echo   Urban Development Coursework
echo ============================================================
echo.

cd /d "%ROOT%"
if errorlevel 1 goto :fail_root

echo [1/5] Pulling latest changes...
git pull --ff-only
if errorlevel 1 goto :fail_git

echo.
echo [2/5] Building StarUML project...
cd /d "%COURSE%"
if errorlevel 1 goto :fail_course

call :python scripts\build_uml.py
if errorlevel 1 goto :fail_build

echo.
echo [3/5] Validating StarUML project...
call :python scripts\validate_uml.py "dist\urban_development.uml" --registry "model\registry.json" --forbid "кредит" --forbid "заявк" --forbid "платеж" --forbid "банков"
if errorlevel 1 goto :fail_validate

echo.
echo [4/5] Running methodology audit...
call :python scripts\audit_functionality.py "dist\urban_development.uml" --traceability "model\traceability.json"
if errorlevel 1 goto :fail_audit

echo.
echo [5/5] Opening StarUML project...
if not exist "%UML%" goto :fail_missing

rem Preferred method: use the Windows .uml file association.
start "" "%UML%"
if errorlevel 1 goto :open_fallback

echo.
echo ============================================================
echo   DONE
echo   Project: %UML%
echo ============================================================
echo.
exit /b 0

:python
where py >nul 2>nul
if not errorlevel 1 (
    py -3 %*
    exit /b %errorlevel%
)

where python >nul 2>nul
if not errorlevel 1 (
    python %*
    exit /b %errorlevel%
)

echo ERROR: Python was not found in PATH.
echo Install Python 3 or add python/py to PATH.
exit /b 1

:open_fallback
echo Windows could not open the .uml association. Trying common StarUML paths...

if exist "%ProgramFiles%\StarUML\StarUML.exe" (
    start "" "%ProgramFiles%\StarUML\StarUML.exe" "%UML%"
    exit /b 0
)

if exist "%ProgramFiles(x86)%\StarUML\StarUML.exe" (
    start "" "%ProgramFiles(x86)%\StarUML\StarUML.exe" "%UML%"
    exit /b 0
)

if exist "%ProgramFiles(x86)%\StarUML 5.0\StarUML.exe" (
    start "" "%ProgramFiles(x86)%\StarUML 5.0\StarUML.exe" "%UML%"
    exit /b 0
)

echo.
echo ERROR: Could not locate StarUML automatically.
echo Open this file manually:
echo %UML%
pause
exit /b 1

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

:fail_build
echo ERROR: UML build failed.
goto :failed

:fail_validate
echo ERROR: UML validation failed.
goto :failed

:fail_audit
echo ERROR: Methodology audit script failed.
goto :failed

:fail_missing
echo ERROR: Built UML file was not found:
echo %UML%
goto :failed

:failed
echo.
echo ============================================================
echo   FAILED
echo ============================================================
echo.
pause
exit /b 1
