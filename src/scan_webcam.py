#!/usr/bin/python
# -*-coding:utf-8-*-
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import time
import sys
import linecache

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

change_res(1920,1080)
while True:
    _, frame = cap.read()
    global data
    data = ""
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        data = obj.data.decode("utf-8")
        cv2.putText(frame, obj.data.decode("utf-8"), (50, 50), font, 2,
                    (255, 255, 255), 3)
        if (obj.data.decode("utf-8")[0:6].lower() == "havlu#") or (obj.data.decode("utf-8")[0:3].lower() == "su#"):
            with open('qrid.txt', 'w+') as f:
                f.write(obj.data.decode("utf-8"))
                cap.release()
                cv2.destroyAllWindows()
            
    cv2.imshow("Devrialem GUI - Scanner", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
