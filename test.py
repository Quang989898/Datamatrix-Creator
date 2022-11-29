import base64
import datetime
import warnings
import numpy as np
import pandas as pd
from flask import *
from PIL import Image
from pylibdmtx import pylibdmtx
import cv2
from pystrich.datamatrix import DataMatrixEncoder
def getjson(dmc):
    encoder = DataMatrixEncoder(dmc)
    # encoder.save("static/images/barcode2.png",50)
    encoder_data = encoder.get_imagedata(50)
    encoded_string= base64.b64encode(encoder_data)

    imgdata = encoded_string.decode('utf-8')
    img = cv2.imread("static/images/blank.png")
    _,img = cv2.imencode(".png",img)
    img = img.tobytes()
    img= base64.b64encode(img)
    img = img.decode('utf-8')
    data = {
        "0":{
            "type":4,
            "content":"<img style='width:35px;height:35px;padding-left:25px;' src='data:image/png;base64," + imgdata + "'>"
        },
        "1":{
            "type":4,
            "content":"<img style='height:13px' src='data:images/png;base64,"+img+"'>"
        }
    }
    return data
print(getjson('abc'))
