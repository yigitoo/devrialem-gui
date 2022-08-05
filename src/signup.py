#!/usr/bin/python
# -*-coding:utf-8-*-
# import tkinter.scrolledtext as scrolledtext
import tkinter
from tkinter import messagebox
import pymongo as mongo
import random as r
from uuid import uuid4 as generate_token

def insert_user(name, surname, username, password):
    db_link = "mongodb+srv://nfl:nfl2021@cluster0.nzqee.mongodb.net/test&ssl=true"
    expression = not (name.get() == "" or surname.get() == "" or password.get() == "" or username.get() == "")
    if expression:
        new_user = {
            "name": name.get(),
            "surname": surname.get(),
            "username": username.get(),
            "password": password.get(),
            "reservations": {},
            "credit": 0,
            "isAdmin": False,
            "code": str(generate_token()),
            "donates": 0
            # add "_id" paramater later with random library and check with dbmodel!:)
        }

        with mongo.MongoClient(db_link) as client:
            table = client["hotel_reservation"]
            db = table.users
            while True:
                random_id = r.randint(100000,999999)
                checkusername = db.find_one({
                    "username": username.get()
                })
                checkuserid = db.find_one({
                    "_id": random_id
                })
                if checkuserid == None and checkuserid == None:
                    new_user["_id"] = random_id
                    userjson = db.insert_one(new_user)
                    if userjson != None:
                        messagebox.showinfo(title="Kayıt başarılı", message="Kayıt olma işlemin başarıyla sonuçlandı.")
                        print(f"Yeni kullanıcı kaydı yapıldı: {name.get() + ' ' + surname.get()}")
                        break
                    else: 
                        messagebox.showerror(title="Bilinmeyen Hata", message="Kayıt oluşturulurken bilinmeyen bir hata meydana geldi.\nTahmin: İnternet bağlantın sağlıklı veya kullanılabilir olmayabilir.")
                if checkusername != None:
                    messagebox.showerror(title="Hata", message="Bu kullanıcı adı alınmış ya da form tam doldurulmamış.")
    else:
        messagebox.showerror(title='Hata', message='Lütfen formun tamamını doldurun!')
                    


root = tkinter.Tk()
def on_closing():
    if messagebox.askokcancel("Çıkış", "Çıkmak istediğine emin misin?"):
        root.destroy()
# root.bind('<Escape>', root.destroy)
root.title('Devrialem GUI')
root.configure(bg='#333333')


frame = tkinter.Frame(bg='#333333')

signup_label = tkinter.Label(
    frame, text="Kayıt ol", bg='#333333', fg="#FF3399", font=("Consolas", 45))

name_label = tkinter.Label(
    frame, text="İsmin:", bg='#333333', fg="#FFFFFF", font=("Consolas", 25))
name = tkinter.StringVar()
name_entry = tkinter.Entry(frame, textvariable=name, font=("Consolas", 25))

surname_label = tkinter.Label(
    frame, text="Soy İsmin:", bg='#333333', fg="#FFFFFF", font=("Consolas", 25))
surname = tkinter.StringVar()
surname_entry = tkinter.Entry(frame, textvariable=surname, font=("Consolas", 25))

username_label = tkinter.Label(
    frame, text="Kullanıcı adı:", bg='#333333', fg="#FFFFFF", font=("Consolas", 25))
username = tkinter.StringVar()
username_entry = tkinter.Entry(frame, textvariable=username, font=("Consolas", 25))

password_label = tkinter.Label(
    frame, text="Şifre:", bg='#333333', fg="#FFFFFF", font=("Consolas", 25))
password = tkinter.StringVar()
password_entry = tkinter.Entry(frame, textvariable=password, show="*", font=("Consolas", 25))

signup_button = tkinter.Button(
    frame, text="Kayıt ol!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25), command=lambda: insert_user(name, surname, username, password))
quit_button = tkinter.Button(
    frame, text="Ana menüye dön!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25), command=on_closing)

# Placing widgets on the screen
signup_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=55)
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1, pady=20)
surname_label.grid(row=2, column=0)
surname_entry.grid(row=2, column=1, pady=20)
username_label.grid(row=3, column=0)
username_entry.grid(row=3, column=1, pady=20)
password_label.grid(row=4, column=0)
password_entry.grid(row=4, column=1, pady=20)
signup_button.grid(row=5, column=0, columnspan=1, pady=30)
quit_button.grid(row=5, column=1, columnspan=1, pady=30)

frame.pack()
menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=on_closing)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.attributes("-fullscreen", True)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()