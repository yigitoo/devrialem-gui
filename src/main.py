#!/usr/bin/python
# -*-coding:utf-8-*-
# coding: utf-8
import tkinter
from tkinter import messagebox
import pymongo as mongo
import os
from tkinter import ttk
import threading
from fingercounter import fingerCounter
from functools import partial
import time
from sounds.lib import play_voice # made by me :D


root = tkinter.Tk()
finger_file = 'fingercount.txt'
with open(finger_file, 'w') as f:
    f.write('')

fc = fingerCounter()
getfingers = partial(fc.getfingers)
thread_getfingers = threading.Thread(target=getfingers, daemon=True) 
 
def delete_fingerfile():
    with open(finger_file, 'w') as f:
        f.write('')

def controlWithMotion():
    try:
        global current_upCount
        thread_getfingers.start()
        while True:
            with open(finger_file, 'r') as f:
                current_upCount = f.read()

                if current_upCount == "5":
                    fc.close = 1
                    delete_fingerfile()
                    time.sleep(2)

                    play_voice('giris')
                    
                    login()
                if current_upCount == "2":
                    delete_fingerfile()
                    
                    play_voice('kayit')

                    signup()
                    delete_fingerfile()
                if current_upCount == "3":
                    delete_fingerfile()
                    version()
                    delete_fingerfile()
    except RuntimeError:
        print('İsteğiniz alındı.')


def on_closing():
    if messagebox.askokcancel("Çıkış", "Çıkmak istediğine emin misin?"):
        root.destroy()
        delete_fingerfile()
# root.bind('<Escape>', root.destroy)
root.title('Devrialem GUI')
root.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')

def login():
    if os.name == "nt":
        os.system('.\\scripts\\win\\login.bat')
    if os.name == "posix":
        os.system('chmod +x ./scripts/linux/login.sh && sh ./scripts/linux/login.sh')
    '''
    # i dont wanna use for macos because i have not money for that :D
    # and who is want to use this system on macOS :D whatever i dont add for
    # darwin :D
    '''
    raise SystemExit

def signup():
    os.system('python signup.py')

# tlogin = threading.Thread(target=login)
# tsignup = threading.Thread(target=signup)

def version():
    messagebox.showinfo(title="Version", message=f"""Version 1.1
Hazırlayan: Yiğit GÜMÜŞ
Sistem: Devrialem
Yarışma Alanı: Turizm Teknolojileri
Yarışma: #TEKNOFEST2022""")

# Creating widgets
title_label = tkinter.Label(
    frame, text=f"Devrialem sistemine hoşgeldin!", bg='#333333', fg="#FF3399", font=("Consolas", 45))
title_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=50)


giris_button = tkinter.Button(
    frame, text="Giriş yap!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
giris_button.grid(row=1,column=0, sticky="news", ipadx=75,ipady=50)
giris_button.config(command=login) #lambda: tlogin.start()

kayit_button = tkinter.Button(
    frame, text="Kayıt ol!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
kayit_button.grid(row=1,column=1, sticky="news", ipadx=75,ipady=50)
kayit_button.config(command=signup) #lambda: tsignup.start()


version_button= tkinter.Button(
    frame, text="Versiyon", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
version_button.grid(row=2,column=0, sticky="news", ipadx=75,ipady=50)
version_button.config(command=version)

quit_button = tkinter.Button(
    frame, text="Çıkış!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
quit_button.grid(row=2,column=1, sticky="news",ipadx=75,ipady=50)
quit_button.config(command=on_closing)

frame.pack()

menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=on_closing)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

thread_controlWithMotion = threading.Thread(target=controlWithMotion, daemon=True)
thread_controlWithMotion.start()

root.attributes("-fullscreen", True)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()