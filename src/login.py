# import tkinter.scrolledtext as scrolledtext
import tkinter
from tkinter import messagebox
from functools import partial
import pymongo as mongo
import os

def validateLogin(username, password, db_link):
    global usrname
    usrname = username.get()
    passwd = password.get()

    with mongo.MongoClient(db_link) as client:
        table = client["hotel_reservation"]
        db = table.users
        json_obj = db.find_one({
            "username": usrname,
            "password": passwd
        })
        if json_obj == None:
            messagebox.showerror(title="Error", message="Yanlış kullanıcı adı veya şifre.")
        else:
            print(json_obj)
            fullname = json_obj["name"] + " " + json_obj["surname"]
            messagebox.showinfo(title="Login Success", message=f"Hoşgeldin \"{fullname}\", adına giriş yapıldı.")
            username_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)
            with open('username.txt', 'w', encoding='utf-8') as f:
                f.write(f"{fullname}\n{json_obj['username']}\n{json_obj['_id']}")
            os.system("python mainmenu.py")

db_link = "mongodb+srv://nfl:nfl2021@cluster0.nzqee.mongodb.net/test&ssl=true"

root = tkinter.Tk()
def on_closing():
    if messagebox.askokcancel("Çıkış", "Çıkmak istediğine emin misin?"):
        root.destroy()
# root.bind('<Escape>', root.destroy)
root.title('Devrialem GUI')
root.configure(bg='#333333')


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

validateLogin = partial(validateLogin, username, password, db_link)
login_button = tkinter.Button(
    frame, text="Giriş!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25), command=validateLogin)

quit_button = tkinter.Button(
    frame, text="Ana menüye dön!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25), command=on_closing)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=1, pady=30)
quit_button.grid(row=3, column=1, columnspan=1, pady=30)
frame.pack()
menubar = tkinter.Menu(root)
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=on_closing)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.attributes("-fullscreen", True)
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()