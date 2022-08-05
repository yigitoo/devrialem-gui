#!/usr/bin/python
# -*-coding:utf-8-*-
import tkinter
from tkinter import messagebox
import pymongo as mongo
import os
from functools import partial
import linecache
import subprocess
import threading
import time
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sys

# i cut the last char because the file has \0 in last of lines 
# if you are coded in c you'll know the malloc things
# for example: malloc(4) byte [0] => a [1] => b [2] => c [3] => "\0"
name = linecache.getline('username.txt', 1)[:-1]
user = linecache.getline('username.txt', 2)[:-1]
id_ = linecache.getline('username.txt', 3)[:-1]

print(user, id_)
def manipulate_creditplus():
	db_link = "mongodb+srv://nfl:nfl2021@cluster0.nzqee.mongodb.net/test&ssl=true"
	with mongo.MongoClient(db_link) as client:
		db = client['hotel_reservation']['users']
		db.find_one_and_update(
		{
			"username": user,
			"_id": int(id_)
		},
			{"$inc": {"credit": 50} }
		)

		messagebox.showinfo(title="Kredi manipülasyonu başarılı.", message=f'Krediniz "+50" puan artırıldı.')
	
def manipulate_creditminus():
	db_link = "mongodb+srv://nfl:nfl2021@cluster0.nzqee.mongodb.net/test&ssl=true"
	with mongo.MongoClient(db_link) as client:
		table = client["hotel_reservation"]
		db = table.users

		db.find_one_and_update(
			{
			"username": user,
			"_id": int(id_)
		},
			{"$inc": {"credit": -50} }
		)

		messagebox.showinfo(title="Kredi manipülasyonu başarılı.", message=f'Krediniz: "-50" puan azaltıldı.')
	
root = tkinter.Tk()
def on_closing():
    if messagebox.askokcancel("Çıkış", "Çıkmak istediğine emin misin?"):
        root.destroy()
root.bind('<Escape>', root.destroy)
root.title('Devrialem GUI')
root.configure(bg='#333333')

#Creating Widgets
frame = tkinter.Frame(bg='#333333')

title_label = tkinter.Label(
	frame, text = f"Tarayıcı sayfasına hoşgeldin {user}.", bg='#333333', fg='#FF3399', font=('Consolas', 30))
title_label.grid(row=0, column=0, columnspan=2, sticky='news', ipady=75)

ncredit_buttonminus = tkinter.Button(
    frame, text="-", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
ncredit_buttonminus.grid(row=2, column=1, sticky="news", columnspan=1, pady=20, ipady=40)
ncredit_buttonminus.config(command=manipulate_creditminus)

ncredit_buttonplus = tkinter.Button(
    frame, text="+", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
ncredit_buttonplus.grid(row=2, column=0, sticky="news", columnspan=1, pady=20, ipady=40)
ncredit_buttonplus.config(command=manipulate_creditplus)

def textloop():
	with open("qrid.txt", "r") as t:
		scanner_data.config(text=f'Son Taranan veri: {t.read()}')
	root.after(500, textloop)
scanner_data = tkinter.Button(
    frame, text="Veri taranmadı.", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
scanner_data.grid(row=3, column=0, sticky="news", columnspan=2, pady=20)

back_button = tkinter.Button(
	frame, text="Geri dön!", bg='#FF3399', fg='#FFFFFF', font = ("Consolas", 25))
back_button.config(command=on_closing)
back_button.grid(row=1, column=1, sticky='news', ipadx=100, ipady=50)
def open_scanner():
	os.system('python scan_webcam.py')

topen_scanner = threading.Thread(target=open_scanner)

opencam_button = tkinter.Button(
    frame, text="Kamerayı aç.", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
opencam_button.grid(row=1,column=0, sticky="news", ipadx=100,ipady=50)
opencam_button.config(command=lambda: topen_scanner.start()) #open_scanner


frame.pack()
menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=on_closing)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.attributes('-fullscreen', True)
root.protocol('WM_DELETE_WINDOW', on_closing)
textloop()
root.mainloop()