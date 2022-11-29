import cv2
from pylibdmtx import pylibdmtx
import numpy as np
video = cv2.VideoCapture(0)
address = 'https:192.168.124.128:8080/video'
video.open(address)
while True:
    check,frame=video.read()
    # img = cv2.resize(frame,(800,600))
    img = frame[500:1000,500:1000]
    msg = pylibdmtx.decode(frame)
    cv2.imshow("abc",img)
    cv2.waitKey(1)
    print(msg)
