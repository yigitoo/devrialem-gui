import tkinter
from tkinter import messagebox
import pymongo as mongo
import os

with open('username.txt', 'r', encoding="utf-8") as f:
    user = f.readlines()[0]

root = tkinter.Tk()
def open_website(): 
    os.system('python open_website.py')
def version():
    messagebox.showinfo(title="Version", message=f"""Version 1.1
Hazırlayan: Yiğit GÜMÜŞ
Sistem: Devrialem
Yarışma Alanı: Turizm Teknolojileri
Yarışma: #TEKNOFEST2022""")
def scan_qr_gui():
    os.system('python scan_qr_gui.py')
def signup():
    os.system('python sign_up.py')
def on_closing():
    if messagebox.askokcancel("Çıkış", "Çıkmak istediğine emin misin?"):
        root.destroy()
root.bind('<Escape>', root.destroy)
root.title('Devrialem GUI')
root.configure(bg='#333333')

frame = tkinter.Frame(bg='#333333')

# Creating widgets
title_label = tkinter.Label(
    frame, text=f"Hoşgeldin, {user}!", bg='#333333', fg="#FF3399", font=("Consolas", 45))
title_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)

qrcode_button = tkinter.Button(
    frame, text="QrCode okut.", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
qrcode_button.grid(row=1,column=0, sticky="news", ipadx=40,ipady=40)
qrcode_button.config(command=scan_qr_gui)

site_button= tkinter.Button(
    frame, text="Uygulamayı aç!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
site_button.grid(row=1,column=1, sticky="news", ipadx=40,ipady=40)
site_button.config(command=open_website)

version_button = tkinter.Button(
    frame, text="Edisyon.", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
version_button.grid(row=2,column=0, sticky="news", ipadx=40,ipady=40)
version_button.config(command=version)

quit_button = tkinter.Button(
    frame, text="Geri dön!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
quit_button.grid(row=2,column=1, sticky="news",ipadx=40,ipady=40)
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