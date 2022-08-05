echo off
taskkill /f /im "python.exe"
(python3 scan_qr_gui.py || python scan_qr_gui.py)
echo on