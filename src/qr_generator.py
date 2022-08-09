import tkinter as tk
from PIL import Image,ImageTk
import pyqrcode
from tkinter.font import Font
import random
from functools import partial
import pymongo
import time

class QRCodeLabel(tk.Label):
    def __init__(self, parent, qr_data):
        super().__init__(parent)
        print('QRCodeLabel("{}")'.format(qr_data))
        qrcode = pyqrcode.create(qr_data)
        tmp_png_file = "QRCode.png"
        qrcode.png(tmp_png_file, scale=8)
        self.image = tk.PhotoImage(file=tmp_png_file)
        self.configure(image=self.image)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.site = {
            'product': 'https://devrialem.vercel.app',
            'dev': 'http://localhost:3000'
        }
        self.title("QR kod oluşturucu")
        self.choice = 'product'
        self.totp_list = []
        buttonQR = tk.Button(text="Giriş Karekodu Oluştur!", font=("", 30), bg="white", command=self.generateQR)
        buttonQR.grid(row=2, column=0)
        self.qr_label = None

        #self.attributes("-fullscreen", True)
        self.eval('tk::PlaceWindow . center')
        self.partial_delete_totp_to_db_and_exit = partial(self.delete_totp_to_db_and_exit, self.totp_list)
        self.protocol("WM_DELETE_WINDOW", self.partial_delete_totp_to_db_and_exit)
        self.mainloop()


    def write_totp_to_db(self, num):
        self.num = num
        with pymongo.MongoClient("mongodb+srv://nfl:nfl2021@cluster0.nzqee.mongodb.net/test&ssl=true") as client:
            db = client["hotel_reservation"]["totp"]
            json_obj = db.find_one({"_id": self.num})
            if json_obj == None:
                db.insert_one({"_id": self.num})
    
    def delete_totp_to_db_and_exit(self, numberlist):
        self.numberlist = numberlist
        with pymongo.MongoClient("mongodb+srv://nfl:nfl2021@cluster0.nzqee.mongodb.net/test&ssl=true") as client:
            db = client['hotel_reservation']['totp']
            for i in self.numberlist:
                db.delete_one({"_id": i})
        
        time.sleep(1)
        self.destroy()
            
    def generateQR(self):
        if self.qr_label:
            self.qr_label.destroy()

        self.totp_number = random.randint(100000,999999)
        self.write_totp_to_db(self.totp_number)
        self.totp_list.append(self.totp_number)
        self.link = f'{self.site[self.choice]}/login/{self.totp_number}'
        self.qr_label = QRCodeLabel(self, self.link)
        self.qr_label.grid(row=1, column=0)


if __name__ == "__main__":
    App().mainloop()