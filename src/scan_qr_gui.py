import tkinter
from tkinter import messagebox
import pymongo as mongo
import os
from functools import partial
import linecache
from tkinter import NORMAL, DISABLED
import subprocess

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
	frame, text = f"Tarayıcı sayfasına hoşgeldin {user}", bg='#333333', fg='#FF3399', font=('Consolas', 30))
title_label.grid(row=0, column=0, columnspan=2, sticky='news', pady=50)

ncredit_buttonminus = tkinter.Button(
    frame, text="-", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25), state=DISABLED)
ncredit_buttonminus.grid(row=2, column=1, sticky="news", columnspan=1, pady=20)
ncredit_buttonminus.config(command=manipulate_creditminus, state=DISABLED)

ncredit_buttonplus = tkinter.Button(
    frame, text="+", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25), state=DISABLED)
ncredit_buttonplus.grid(row=2, column=0, sticky="news", columnspan=1, pady=20)
ncredit_buttonplus.config(command=manipulate_creditplus, state=DISABLED)


back_button = tkinter.Button(
	frame, text="Geri dön!", bg='#FF3399', fg='#FFFFFF', font = ("Consolas", 25))
back_button.config(command=on_closing, state=NORMAL)
back_button.grid(row=3,column=0, sticky="news", ipadx=40,ipady=40, columnspan=3)
def scan_webcam():
	ncredit_buttonminus['state'] = NORMAL
	ncredit_buttonplus['state'] = NORMAL
	os.system('python scan_webcam.py')

opencam_button = tkinter.Button(
    frame, text="Kamerayı aç.", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
opencam_button.grid(row=1,column=0, sticky="news", ipadx=40,ipady=40)
opencam_button.config(command=scan_webcam)

def close_webcam():
	prog = subprocess.Popen(['python', 'scan_webcam.py'])
	prog.terminate()

closecam_button = tkinter.Button(
    frame, text="Kamerayı kapat.", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
closecam_button.grid(row=1, column=1, sticky='news', ipadx=50, ipady=50)
closecam_button.config(command=close_webcam)



frame.pack()
menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=on_closing)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.attributes('-fullscreen', True)
root.protocol('WM_DELETE_WINDOW', on_closing)
root.mainloop()