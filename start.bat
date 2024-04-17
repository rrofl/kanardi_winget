@echo off
setlocal enableextensions

echo Detecting administrative permissions...

:: Check if the script is run with administrative privileges
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: This script requires administrative permissions to run. Exiting...
    pause
    exit /B 1
)

:: Set path to script location
cd /d "%~dp0"

:: Check if the file already exists
if not exist "winget.msixbundle" (
    echo Downloading winget.msixbundle...
    powershell -Command "(New-Object Net.WebClient).DownloadFile('https://aka.ms/getwinget', 'winget.msixbundle')"
    if %errorlevel% neq 0 (
        echo ERROR: Failed to download winget.msixbundle. Please check your internet connection or try again later.
        pause
        exit /B 1
    )
) else (
    echo winget.msixbundle already exists. Skipping download.
)

:: Install Winget
echo Installing Winget...
powershell -Command "Add-AppxPackage -Path 'winget.msixbundle'"
if %errorlevel% neq 0 (
    echo ERROR: Failed to install Winget. The system will reboot. Please run the script again.
    pause
    shutdown /r /t 0
    exit /B 1
)

echo Installation completed.

C:\Users\rrofl\AppData\Local\Programs\Python\Python311\python.exe %~d0\Projects\Kanardi\winget_ctk.py