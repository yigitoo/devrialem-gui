#!/usr/bin/python
# -*-coding:utf-8-*-
import pyautogui as keyboard
import os
import time

def redirect(site):
	if os.name == "nt":
		os.system(f'start chrome "{site}"')
	if os.name == "posix":
		os.system(f'xdg-open {site}')
site = {
	"product": "http://devrialem.vercel.app",
	"dev": "localhost:3000"
}

choice = "product"

try:
	redirect(site[choice])

	time.sleep(3)
	keyboard.press('f11')
	time.sleep(150)
	keyboard.hotkey('alt', 'f4')
except Exception as e:
	print(e)
except KeyboardInterrupt:
	print("Exiting...")