#!/usr/bin/python3
# -*-coding:utf-8-*-
import tkinter
from tkinter import messagebox
import pymongo as mongo
import os
from tkinter import ttk
import threading

root = tkinter.Tk()
root.title('Devrialem GUI - #Teknofest2022')
root.configure(bg='#333333')

def on_closing():
    if messagebox.askokcancel("Çıkış", "Çıkmak istediğine emin misin?"):
        root.destroy()
# root.bind('<Escape>', root.destroy)
def mainapp():
    os.system('python main.py')
frame = tkinter.Frame(bg='#333333')
# Creating widgets
title_label = tkinter.Label(
    frame, text=f"Devrialem sistemine hoşgeldin!", bg='#333333', fg="#FF3399", font=("Consolas", 45))
title_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=75)

logapp_button = tkinter.Button(
    frame, text="Uygulamayı kullan!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25)
)
logapp_button.grid(row=1,column=0, sticky="news",ipadx=75,ipady=75)
logapp_button.config(command=mainapp)

quit_button = tkinter.Button(
    frame, text="Çıkış!", bg="#FF3399", fg="#FFFFFF", font=("Consolas", 25))
quit_button.grid(row=1,column=1, sticky="news",ipadx=75,ipady=75)
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