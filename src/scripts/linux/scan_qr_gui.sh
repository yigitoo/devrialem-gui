#!/usr/bin/sh
pkill -9 -f mainmenu.py
python3 ../../scan_qr_gui.py || python ../../scan_qr_gui.py