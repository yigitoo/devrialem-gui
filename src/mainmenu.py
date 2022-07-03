#!/usr/bin/python
# -*-coding:utf-8-*-
import tkinter
from tkinter import messagebox

from numpy import sign
import pymongo as mongo
import os
import linecache
import threading

name = linecache.getline('username.txt', 1)[:-1]
user = linecache.getline('username.txt', 2)[:-1]
id_ = linecache.getline('username.txt', 3)[:-1]

root = tkinter.Tk()
def open_website(): 
    os.system('python open_website.py')
topen_website = threading.Thread(target=open_website)
def user_page():
    db_link = "mongodb+srv://nfl:nfl2021@cluster0.nzqee.mongodb.net/test&ssl=true"
    with mongo.MongoClient(db_link) as client:
        db = client["hotel_reservation"]["users"]
        user_json = db.find_one(
        {
            "username": user,
            "_id": int(id_)        
        })
        if user_json["isAdmin"] == True:
            adminize = "Admin"
        else:
            adminize = "Kullanıcı"
        messagebox.showinfo(title="Kullanıcı bilgileri", message=f"""-------------
Kullanıcı Adı: {user_json["username"]}
İsim: {user_json['name']}
Soy İsim: {user_json['surname']}
Kredi: {user_json["credit"]}
Üye Tipi: {adminize}
""")

def scan_qr_gui():
    os.system('python scan_qr_gui.py')
tscan_qr_gui = threading.Thread(target=scan_qr_gui)

def on_closing():
    if messagebox.askokcancel("Çıkış", "Çıkmak istediğine emin misin?"):
        root.destroy()
root.bind('<Escape>', root.destroy)
root.title('Devrialem GUI')
root.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')

# Creating widgets
title_label = tkinter.Label(
    frame, text=f"Hoşgeldin, {name}!", bg='#333333', fg="#FF3399", font=("Consolas", 45))
title_label.grid(row=0, column=0, columnspan=2, sticky="news", ipadx=150, pady=75)

qrcode_button = tkinter.Button(
    frame, text="Tarayıcı aç.", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
qrcode_button.grid(row=1,column=0, sticky="news", ipadx=75,ipady=75)
qrcode_button.config(command=lambda: tscan_qr_gui.start())

site_button= tkinter.Button(
    frame, text="Uygulamayı aç!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
site_button.grid(row=1,column=1, sticky="news", ipadx=100,ipady=75)
site_button.config(command=lambda: topen_website.start())

userpage_button = tkinter.Button(
    frame, text="Kullanıcı Bilgileri.", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
userpage_button.grid(row=2,column=0, sticky="news", ipadx=75,ipady=75)
userpage_button.config(command=user_page)

quit_button = tkinter.Button(
    frame, text="Geri dön!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
quit_button.grid(row=2,column=1, sticky="news",ipadx=100,ipady=75)
quit_button.config(command=on_closing)
frame.pack()

menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=on_closing)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.attributes("-fullscreen", True)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()