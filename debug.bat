@echo off

cd C:\Users\Jonathan\My Documents\GitHub\Roguelike
main.py

if not errorlevel 1 goto quit
echo.
echo.
pause
:quit