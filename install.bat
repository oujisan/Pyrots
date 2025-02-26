@echo off
set SCRIPT_DIR=%~dp0
set SCRIPT_DIR=%SCRIPT_DIR:~0,-1%
setx PATH "%SCRIPT_DIR%;%PATH%"
echo PyROTS has been successfully installed! You can run it using: pyrots.
