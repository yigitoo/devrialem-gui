#!/usr/bin/python
# -*-coding:utf-8-*-
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import time
import sys
import linecache
import pymongo
import os

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

closefile = 0
class Login(object):
    def __init__(self, close = 0):
        self.close = 0

    def validateLogin(self, person):
        global closefile
        with pymongo.MongoClient("mongodb+srv://nfl:nfl2021@cluster0.nzqee.mongodb.net/test&ssl=true") as client:
            collections = client["hotel_reservation"]
            db = collections.users

            json_obj = db.find_one({
                "code": str(person)
            })
            fullname = json_obj['name'] +" "+ json_obj['surname']
            if json_obj != None:
                with open('username.txt', 'w', encoding="UTF-8") as f:
                    f.write(f"{fullname}\n{json_obj['username']}\n{json_obj['_id']}")
                if os.name == "nt":   
                    cap.release()
                    cv2.destroyAllWindows()

                    self.close = 1
                    
                    time.sleep(2)
                    
                    os.system('.\\scripts\\win\\mainmenu.bat')


                    raise SystemExit
                if os.name == "posix":      
                    cv2.destroyAllWindows()
                    cap.release()
                    
                    self.close = 1
                    
                    time.sleep(2)
                    os.system('chmod +x ./scripts/linux/mainmenu.sh && sh ./scripts/linux/mainmenu.sh')
                    

    def change_res(self, width, height):
        cap.set(3, width)
        cap.set(4, height)

    def camloop(self):
        self.change_res(1920,1080)
        while True:
            _, frame = cap.read()
            global data
            data = ""
            decodedObjects = pyzbar.decode(frame)
            for obj in decodedObjects:
                data = obj.data.decode("utf-8")
                cv2.putText(frame, obj.data.decode("utf-8"), (50, 50), font, 2,
                            (255, 255, 255), 3)
                
                self.validateLogin(data)

            cv2.imshow("Devrialem GUI - Login", frame)

            key = cv2.waitKey(1)
            if key == ord('q'):
                break

            if self.close == 1:
                break
if __name__ == '__main__':
    login = Login()
    login.camloop()