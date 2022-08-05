echo off
taskkill /f /im "python.exe"
(python3 login.py || python login.py)
echo on