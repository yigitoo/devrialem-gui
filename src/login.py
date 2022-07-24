#!/usr/bin/python
# -*-coding:utf-8-*-
# import tkinter.scrolledtext as scrolledtext
import tkinter
from tkinter import messagebox
from functools import partial
import threading
import pymongo as mongo
import os
import platform

def validateLogin(username, password):
    global usrname
    usrname = username.get()
    passwd = password.get()

    with mongo.MongoClient("mongodb+srv://nfl:nfl2021@cluster0.nzqee.mongodb.net/test&ssl=true") as client:
        table = client["hotel_reservation"]
        db = table.users
        json_obj = db.find_one({
            "username": usrname,
            "password": passwd
        })
        if json_obj == None:
            messagebox.showerror(title="Error", message="Yanlış kullanıcı adı veya şifre. Lütfen formun TAMAMINI ve verileri DOĞRU girin. :)")
        else:
            print(json_obj)
            fullname = json_obj["name"] + " " + json_obj["surname"]
            messagebox.showinfo(title="Login Success", message=f"Hoşgeldin \"{fullname}\", adına giriş yapıldı.")
            username_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            with open('username.txt', 'w', encoding='utf-8') as f:
                f.write(f"{fullname}\n{json_obj['username']}\n{json_obj['_id']}")
            os.system("python mainmenu.py")
root = tkinter.Tk()
def on_closing():
    if messagebox.askokcancel("Çıkış", "Çıkmak istediğine emin misin?"):
        root.destroy()
# root.bind('<Escape>', root.destroy)
root.title('Devrialem GUI')
root.configure(bg='#333333')

def login_with_qr_code():
    operating_system = platform.system().lower()
    if operating_system == "linux":
        os.system('xdg-open https://devrialem.vercel.app/auth/qrlogin/')
    if operating_system == "windows":
        try:
            os.system('start chrome https://devrialem.vercel.app/auth/qrlogin/')
        except:
            os.system('explorer "https://google.com"')
    if operating_system == "darwin": #which mean macOS
        os.system('open https://devrialem.vercel.app/auth/qrlogin/')
tlogin_with_qr_code = threading.Thread(target=login_with_qr_code)
frame = tkinter.Frame(bg='#333333')

# Creating widgets
login_label = tkinter.Label(
    frame, text="Giriş", bg='#333333', fg="#FF3399", font=("Consolas", 45))

username_label = tkinter.Label(
    frame, text="Kullanıcı adı:", bg='#333333', fg="#FFFFFF", font=("Consolas", 25))
username = tkinter.StringVar()
username_entry = tkinter.Entry(frame, textvariable=username, font=("Consolas", 25))

password_label = tkinter.Label(
    frame, text="Şifre:", bg='#333333', fg="#FFFFFF", font=("Consolas", 25))
password = tkinter.StringVar()
password_entry = tkinter.Entry(frame, textvariable=password, show="*", font=("Consolas", 25))

xvalidateLogin = partial(validateLogin, username, password)
# tvalidateLogin = threading.Thread(target=xvalidateLogin)

login_button = tkinter.Button(
    frame, text="Giriş!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25), command=xvalidateLogin)
quit_button = tkinter.Button(
    frame, text="Ana menüye dön!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25), command=on_closing)

login_with_qr_button = tkinter.Button(
    frame, text = 'Karekod ile giriş', bg='#FF3399', fg='#FFFFFF', font = ('Consolas', 25)
)
login_with_qr_button.configure(command=lambda: tlogin_with_qr_code.start())
# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=3, sticky="news", pady=50)
username_label.grid(row=1, column=0, pady=30)
username_entry.grid(row=1, column=1, pady=50)
password_label.grid(row=2, column=0, pady=30)
password_entry.grid(row=2, column=1, pady=50)
login_button.grid(row=3, column=0, columnspan=1, pady=50, padx=10)
quit_button.grid(row=3, column=2, columnspan=1, pady=50)
login_with_qr_button.grid(row=3, column=1, columnspan=1, pady=50)
frame.pack()

menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=on_closing)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.attributes("-fullscreen", True)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()