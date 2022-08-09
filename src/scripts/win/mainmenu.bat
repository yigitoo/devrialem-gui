echo off
taskkill /f /im "python.exe"
(python3 mainmenu.py || python mainmenu.py)
echo on