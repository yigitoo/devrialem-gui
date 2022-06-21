#!/usr/bin/python
# -*-coding:utf-8-*-
import tkinter
from tkinter import messagebox
import pymongo as mongo
import os
from tkinter import ttk

root = tkinter.Tk()

def on_closing():
    if messagebox.askokcancel("Çıkış", "Çıkmak istediğine emin misin?"):
        root.destroy()
# root.bind('<Escape>', root.destroy)
root.title('Devrialem GUI')
root.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')

def login():
    os.system('python login.py')

def signup():
    os.system('python signup.py')

def version():
    messagebox.showinfo(title="Version", message=f"""Version 1.1
Hazırlayan: Yiğit GÜMÜŞ
Sistem: Devrialem
Yarışma Alanı: Turizm Teknolojileri
Yarışma: #TEKNOFEST2022""")

# Creating widgets
title_label = tkinter.Label(
    frame, text=f"Devrialem sistemine hoşgeldin!", bg='#333333', fg="#FF3399", font=("Consolas", 45))
title_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=75)


giris_button = tkinter.Button(
    frame, text="Giriş yap!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
giris_button.grid(row=1,column=0, sticky="news", ipadx=75,ipady=75)
giris_button.config(command=login)

kayit_button = tkinter.Button(
    frame, text="Kayıt ol!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
kayit_button.grid(row=1,column=1, sticky="news", ipadx=75,ipady=75)
kayit_button.config(command=signup)


version_button= tkinter.Button(
    frame, text="Versiyon", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
version_button.grid(row=2,column=0, sticky="news", ipadx=75,ipady=75)
version_button.config(command=version)

quit_button = tkinter.Button(
    frame, text="Çıkış!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
quit_button.grid(row=2,column=1, sticky="news",ipadx=75,ipady=75)
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