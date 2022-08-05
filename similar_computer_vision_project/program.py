#!/usr/bin/python
# -*-coding:utf-8-*-
import cv2
import pyqrcode
from os.path import exists
from os import system, startfile
from random import randint
from threading import Thread
from requests import get
from time import sleep
from playsound import playsound
import vlc
import mediapipe as mp
import numpy as np
import math
from tkinter import *
from tkinter import messagebox
from zipfile import ZipFile
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
area = 0
framelistesi = []
durdur = 0
okubasld=0
kapat = 0
wCam, hCam = 640, 480
pncr=0
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

eller = mp.solutions.hands.Hands(min_detection_confidence=0.5,
                                 min_tracking_confidence=0.5)

surekontrol = 0


def doskont(dosya):
    if exists(dosya):
        return dosya
    else:
        guncelle(1)


def guncelle(m):
    global kapat
    global durdur
    if m == 0:
        messagebox.showinfo("Kitaplığı Güncelle",
                            """
Kitaplığı güncellemek ve yeni içerikleri görebilmek için ok tuşuna basın 
Güncelleme tamalandıktan sonra program güncellemeleri uygulamak için kendini kapatacaktır)
                            """)
    else:
        messagebox.showinfo("Kitaplığı Yenile",
                            "Kitaplık içeriği bozulmuş silinmiş veya görüntülenemiyor içeriyi yenilemek için lütfen ok tuşuna basın")
    url = "https://www.dropbox.com/sh/4y5ueu2ag7odbh2/AADskOhJunXW5qoHytAdBjX0a?dl=1"
    try:
        with get(url, stream=True) as indirilen:
            with open("../Uygulama.zip", 'wb') as zipdosyasi:
                for chunk in indirilen.iter_content(chunk_size=1024):
                    zipdosyasi.write(chunk)
    except IOError:
        messagebox.showinfo("Sunucuya Erişilemedi",
                            "İnternet bağlantınızı kontrol edin ya da programı USB aracılığı ile güncelleyin")
        if isbir.is_alive():
            kapat = 1
            isbir.join()
        if isüc.is_alive():
            kapat = 1
            isüc.join()
        exit()
    rar = ZipFile('../Uygulama.zip')
    rar.extractall()
    messagebox.showinfo("Güncelleme Tamamlandı",
                        "Güncelleme tamamlandı değişikliklerin uygulanabilesi için program kapatılacak")
    if isbir.is_alive():
        kapat = 1
        isbir.join()
    if isüc.is_alive():
        kapat = 1
        isüc.join()
    sleep(5)
    system('yenidenbaslat.bat')
    raise SystemExit

def oku(konum):
    global p
    p = vlc.MediaPlayer(konum)
    p.play()


def ses(yol):
    playsound(yol)


def yazdir(cikti):
    global pncr
    if pncr==1:
        yenip.destroy()
        pncr=0
    elif pncr==2:
        yenip2.destroy()
        pncr=0
    doskont(cikti)
    startfile(cikti,"print")


def karekod(tur, sira):
    yenip2.destroy()
    veri = "veri/qr/" + tur + ".txt"
    sira = int(sira)
    with open(doskont(veri)) as vr:
        for i in range(sira):
            link = vr.readline()
    karekd = pyqrcode.create(link)
    karekdxbm = karekd.xbm(scale=7)
    yenip3 = Toplevel(pencere)
    karekdbmp = BitmapImage(data=karekdxbm)
    karekdbmp.config(background="white")
    label = Label(yenip3, image=karekdbmp)
    label.pack()
    yenip3.mainloop()


def onay(tur, sira):
    global yenip2
    global pncr
    yenip2 = Toplevel(pencere)
    yenip2.geometry("350x150+270+50")
    yenip2.configure(bg="#fce4d7")
    pncr=2
    b1 = Button(yenip2, text="Yazdır", font="Ariel 12 bold", height=8, width=14, bg="#fce4d7",
                command=lambda: yazdir("veri\\B" + tur + "\\" + sira + ".pdf"),
                relief=FLAT)
    b1.grid(row=0, column=0, padx=10)
    b2 = Button(yenip2, text="İnternet Üzerinden \n Dinle", font="Ariel 12 bold", height=8, width=14, bg="#fce4d7",
                command=lambda: karekod(tur, sira),
                relief=FLAT)
    b2.grid(row=0, column=1, padx=10)


def yenipbuton(butondeger):
    global kategori
    liste.delete(0, END)
    with open(doskont("veri/listbox/kategori{}.txt".format(butondeger)), encoding='utf=8') as metinlistesi:
        for baslik in metinlistesi:
            liste.insert("end", baslik[:-1])
    kategori = str(butondeger)


def yenipencere(n):
    global liste
    global yenip
    global kategori
    global pncr
    yenip = Toplevel(pencere)
    yenip.geometry("500x500+270+50")
    liste = Listbox(yenip, selectmode=SINGLE)
    pncr=1
    if n == 1:
        kategori = 9
        butonisim = open(doskont("veri/listbox/Butonisim1.txt"), encoding='utf=8')
        bas = 6
        bit = 9
    else:
        kategori = 0
        butonisim = open(doskont("veri/listbox/Butonisim2.txt"), encoding='utf=8')
        bas = 1
        bit = 6
    Button(yenip, text="seç", width=20, height=3, bg="#A9CCE3", command=secim, relief=FLAT).pack(side=BOTTOM, fill=X)
    yframe = Frame(yenip, bg="#A9CCE3")
    yframe.pack(side=BOTTOM, fill=X)
    for e in range(bas, bit):
        with open(doskont("veri/listbox/kategori{}.txt".format(e)), encoding='utf=8') as Hikayelistesi:
            for baslik in Hikayelistesi:
                liste.insert("end", baslik[:-1])
        Grid.columnconfigure(yframe, e, weight=1)
        Button(yframe, text=butonisim.readline()[:-1], height=3, bg="#A9CCE3", command=lambda x=e: yenipbuton(x),
               relief=FLAT).grid(row=0, column=e, sticky="NSEW")
    butonisim.close()
    kaydirmacubugu = Scrollbar(yenip, command=liste.yview, bg="#009393", troughcolor="#6699FF", width=20)
    liste.config(yscrollcommand=kaydirmacubugu.set)
    kaydirmacubugu.pack(side=RIGHT, fill=Y)
    liste.pack(side=TOP, fill=BOTH, expand=YES)


def indexbul(indexdos, secilenhikaye):
    with open(doskont(indexdos)) as hikayeindex:
        for i in range(secilenhikaye):
            sayi = hikayeindex.readline()
            for j in range(len(sayi)):
                if sayi[j] == " ":
                    tur = sayi[0:j]
                    sira = sayi[j + 1:-1]
                    break
    yazdir("veri\\B" + tur + "\\" + sira + ".pdf")


def secim():
    secilenhikaye = liste.curselection()
    if len(secilenhikaye) == 0:
        return
    secilenhikaye = secilenhikaye[0] + 1
    if kategori == 0:
        indexdos = doskont("veri/listbox/hikayeindex.txt")
        indexbul(indexdos, secilenhikaye)
    elif kategori == 9:
        indexdos = doskont("veri/listbox/şehirindex.txt")
        indexbul(indexdos, secilenhikaye)
    else:
        sira = str(secilenhikaye)
        yazdir("veri\\B" + kategori + "\\" + sira + ".pdf")
    yenip.destroy()


def hikayesec(x, sesktrl=0):
    if x == 6:
        yenipencere(1)
        return
    with open(doskont("veri/S/S{}.txt".format(x)), encoding='utf=8') as s:
        s = int(s.read())
    sayi = randint(1, s)
    sayi=str(sayi)
    if x != 7:
        if sesktrl == 0:
            x = str(x)
            onay(x, sayi)
        else:
            oku("veri/SES{}/{}.mp3".format(x, sayi))
    else:
        yazdir("veri\\B9\\" + sayi + ".pdf")


def yardim():
    yardimp = Toplevel(pencere)
    yardimp.geometry("450x300+320+100")
    with open(doskont("veri/giris.txt"), encoding='utf=8') as giris:
        Label(yardimp, text=giris.read()).pack()


def is2():
    global surekontrol
    playsound(doskont("veri/yuz.mp3"))
    sleep(60)
    surekontrol = 0


idler = [4, 8, 12, 16, 20]
isbir = Thread(target=ses)


def parmakkonum(kr, handNo=0):
    lmList = []
    xList = []
    yList = []
    bbox = []
    RGBkare = cv2.cvtColor(kr, cv2.COLOR_BGR2RGB)
    results = eller.process(RGBkare)
    if results.multi_hand_landmarks:
        el = results.multi_hand_landmarks[handNo]
        for id, lm in enumerate(el.landmark):
            h, w, c = kare.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            xList.append(cx)
            yList.append(cy)
            lmList.append([id, cx, cy])
        xmin, xmax = min(xList), max(xList)
        ymin, ymax = min(yList), max(yList)
        bbox = xmin, ymin, xmax, ymax
    return lmList, bbox


def parmaksay(kr):
    global parmaklar
    global lmList
    global bbox
    lmList, bbox = parmakkonum(kr)

    if len(lmList) != 0:
        parmaklar = []

        if lmList[idler[0]][1] > lmList[idler[0] - 1][1]:
            parmaklar.append(1)
        else:
            parmaklar.append(0)

        for id in range(1, 5):
            if lmList[idler[id]][2] < lmList[idler[id] - 2][2]:
                parmaklar.append(1)
            else:
                parmaklar.append(0)

        sayi = parmaklar.count(1)
        return sayi

def uzaklikbul(lmList):
    x1, y1 = lmList[4][1],lmList[4][2]
    x2, y2 = lmList[8][1],lmList[8][2]
    uzaklik = math.hypot(x2 - x1, y2 - y1)
    return uzaklik

def seskontrol():
    ses("veri/seskontrol.mp3")
    while True:
        s=parmaksay(kare)
        if len(lmList) != 0:
            area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
            if 250 < area < 1000:
                uzaklik=uzaklikbul(lmList)
                volPer = np.interp(uzaklik, [50, 200], [0, 100])
                smoothness = 10
                volPer = smoothness * round(volPer / smoothness)
                if parmaklar==[1,1,1,1,0]:
                    ses("veri/sesayar.mp3")
                    volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                if parmaklar==[1,1,0,0,1]:
                    ses("veri/sescikis.mp3")
                    break

def kategorisec():
    ses("veri/giris.mp3")
    sleep(3)
    syi = parmaksay(kare)
    dlistesi=[1,2,3,4,5]
    if syi in dlistesi :
        if syi==2 and parmaklar ==[1,1,0,0,0]:
            seskontrol()
        else:
            ses("veri/{}.mp3".format(syi))
            ses("veri/scm.mp3")
            sleep(3)
            onayla = parmaksay(kare)
            if onayla == 5:
                hikayesec(syi, 1)
            else:
                ses("veri/iptal.mp3")
    else:
        ses("veri/iptal.mp3")

def elalgıla():
    algsure = 0
    algsure2=0
    while True:
        if kapat == 1:
            break
        syi = parmaksay(kare)
        if algsure == 3:
            algsure = 0
            if p.get_state() in ([3]):
                p.pause()
                continue
            elif p.get_state() in ([4]):
                p.play()
                continue
            kategorisec()
        elif algsure2==3:
            algsure=0
            algsure2=0
            p.stop()
        elif syi == 5:
            algsure += 1
            sleep(1)
        elif syi==3:
            algsure2+=1
            sleep(1)
        else:
            algsure = 0
            sleep(0.5)


def yuzalgila(kare):
    global surekontrol
    cascadexml = cv2.CascadeClassifier('veri/haarcascade_frontalface_default.xml')
    gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)
    yuz = cascadexml.detectMultiScale(gri, scaleFactor=1.2, minNeighbors=5)
    if len(yuz) != 0 and surekontrol == 0:
        isiki = Thread(target=is2, daemon=True)
        isiki.start()
        surekontrol = 1


def kamera():
    global kare
    while cap.isOpened():
        _, kare = cap.read()
        if not _:
            sleep(1)
            continue
        if durdur == 0:
            yuzalgila(kare)
        if kapat == 1:
            break
        cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()


def kamerakont():
    global sessec
    global durdur
    with open(doskont("veri/S/kamera.txt")) as kameradurum:
        kameradurum = kameradurum.read()
        if kameradurum == "1":
            durdur = 0
            sessec = IntVar(value=1)
        else:
            sessec = IntVar()
            durdur = 1


def kamayar():
    global durdur
    ayar = str(sessec.get())
    with open(doskont("veri/S/kamera.txt"), "w") as kamera:
        kamera.write(ayar)
    if ayar == "1":
        durdur = 0
    else:
        durdur = 1


surekontrol = 0

pencere = Tk()
pencere.attributes('-fullscreen', True)
kamerakont()
isbir = Thread(target=kamera)
isbir.start()
sleep(3)
isüc = Thread(target=elalgıla, daemon=True)
isüc.start()
pencere.geometry("1024x600")
pencere.title("Öykü Durağı")
pencere.configure(bg="#f4af85")
oku('veri/acilis.mp3')
ustmenu = Menu(pencere)
secenekler = Menu(ustmenu, tearoff=0)
secenekler.add_command(label="Kitaplığı (yenile) güncelle", command=lambda: guncelle(0))
secenekler.add_checkbutton(label="Sesli Uyarı Açık", variable=sessec, onvalue=1, offvalue=0, command=kamayar)
ustmenu.add_cascade(label="Seçenekler", menu=secenekler)
pencere.config(menu=ustmenu)
for i in range(4):
    framelistesi.append(Frame(relief=FLAT, bg="#f4af85"))
    framelistesi[i].grid(row=i, column=0, sticky="NSEW")
baslik = Label(framelistesi[0], text="Öykü Durağı", bg="#f4af85", font="Ariel 24 bold").pack()

for i in range(3):
    for z in range(3):
        Grid.columnconfigure(framelistesi[i + 1], z, weight=1)
    Grid.rowconfigure(framelistesi[i + 1], 0, weight=1)
    Grid.rowconfigure(pencere, i + 1, weight=1)
Grid.columnconfigure(pencere, 0, weight=1)
with open(doskont("veri/S/B.txt"), encoding='utf=8') as b:
    for j in range(7):
        if j <= 2:
            buton = Button(framelistesi[1], text=b.readline()[:-1], font="Ariel 17 bold", width=5, height=5,
                           relief=FLAT,
                           bg=b.readline()[:-1], command=lambda x=j + 1: hikayesec(x))
            buton.grid(row=0, column=j, padx=7, pady=7, sticky="NSEW")
        elif 2 < j <= 5:
            buton = Button(framelistesi[2], text=b.readline()[:-1], font="Ariel 17 bold", width=5, height=5,
                           relief=FLAT,
                           bg=b.readline()[:-1], command=lambda x=j + 1: hikayesec(x))
            buton.grid(row=0, column=j - 3, padx=7, pady=7, sticky="NSEW")
        else:
            buton = Button(framelistesi[3], text=b.readline()[:-1], font="Ariel 17 bold", width=5, height=5,
                           relief=FLAT,
                           bg=b.readline()[:-1], command=lambda x=j + 1: hikayesec(x))
            buton.grid(row=0, column=j - 6, padx=7, pady=7, sticky="NSEW")

buton = Button(framelistesi[3], text="Kendim Seçmek İstiyorum", font="Ariel 17 bold", width=5, height=5, relief=FLAT,
               bg="#fce4d7", command=lambda: yenipencere(2))
buton.grid(row=0, column=1, padx=7, pady=7, sticky="NSEW")
buton = Button(framelistesi[3], text="Öykü Durağı Nasıl \n Kullanılır?", font="Ariel 17 bold", width=5, height=5,
               relief=FLAT,
               bg="#fce4d7", command=yardim)
buton.grid(row=0, column=2, padx=7, pady=7, sticky="NSEW")
pencere.mainloop()

if isbir.is_alive():
    kapat = 1
    isbir.join()
if isüc.is_alive():
    kapat = 1
    isüc.join()

