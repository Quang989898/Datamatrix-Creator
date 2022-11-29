import base64
import datetime
import warnings
import numpy as np
import pandas as pd
from flask import *
from PIL import Image
from pylibdmtx import pylibdmtx
import cv2
import pyodbc
import time
Quang=""
warnings.filterwarnings("ignore")
from pystrich.datamatrix import DataMatrixEncoder

# conn = pyodbc.connect(
#             'Driver={SQL Server}; Server=WIN-1SJHDOU69JS; ;Database=DMC;uid=sa; pwd=P@ssw0rd; Trusted_Connection=No;')
# cursor = conn.cursor()
def str4(n): # sửa chuỗi có ít hơn 4 ký tự
    n = str(n)
    while len(n)<4:
        n = '0' + n
    return n
def getserial(mahang):
    data = pd.read_csv('serial.csv',index_col=0)
    serial = data.loc[mahang,'Serial']
    data.loc[mahang,'Serial']=data.loc[mahang,'Serial']+1
    data.to_csv('serial.csv')
    return serial
def MAQR(Malo,Productname):
    if malo_str(Malo) != "OK":
        return malo_str(Malo)
    if int(Malo[7:]) >= 10:
        Makhuonsap = Malo[7:]
    else:
        Makhuonsap = "0" + Malo[7:]
    data = pd.read_sql(" select * FROM [DMC].[dbo].[Parameter_DMC]",conn,index_col="ProductName")
    PhienBan = data.loc[Productname,"Version"]
    xulynhiet = data.loc[Productname,"Heat_treatment"]
    serial = data.loc[Productname,"Parameter_setting"]
    MaSX="VC"
    print(PhienBan,xulynhiet,serial)
    Mabanve = data.loc[Productname,"Drawing_code"]
    if PhienBan=="IR":
        Maphienban="I"
    else:
        Maphienban=PhienBan   
    Qrcode=str(serial)+Mabanve[:1]+Mabanve[-6:]+Maphienban+MaSX+Makhuonsap+Malo[:7]+xulynhiet
    if len(Qrcode) != 29:
        return 'Wrong Quantity DMC'
    # #cursor.execute("INSERT INTO [DMC].[dbo].[DMC_Printer] (ProductName,DMC,TimeCreated,Status)VALUES (?,?,?,?)",
    #     Productname,
    #     Qrcode.upper(),
    #     datetime.datetime.now(),
    #     "Fixed DMC"
    # )
    # conn.commit()
    # cursor.execute("Update [DMC].[dbo].[Parameter_DMC] Set Parameter_setting = '"+str(int(serial)+1)+"' Where ProductName='"+Productname+"'" )
    # cursor.commit()
    return Qrcode.upper()
    # encoder = DataMatrixEncoder(Qrcode.upper()).get_imagedata()
    # encoded_string= base64.b64encode(encoder)
    # return encoded_string.decode('utf-8')
def malo_str(malo: str):
    if len(malo)<8 or len(malo)>9:
        return "Wrong Quantity Casting Code"
    elif not malo[7:].isnumeric():
        return "Wrong Wax Mold Code"
    if malo[0].isnumeric():
        year = '202'+malo[0]
    else:
        return 'Wrong Year Code'
    if malo[1].upper() == 'X':
        month = '10'
    elif malo[1].upper() == 'Y':
        month = '11'
    elif malo[1].upper() == 'Z':
        month = '12'
    elif malo[1].isnumeric():
        month = '0'+malo[1]
    else:
        return 'Wrong Month Code'
    if malo[2:4].isnumeric():
        day = malo[2:4]
    else:
        return 'Wrong Day Code'
    if not malo[4].isalpha():
        return 'Wrong Casting Char Code'
    if not malo[5:7].isnumeric():
        return 'Wrong Casting No Code'
    try:
        date = datetime.datetime.strptime(day+month+year,'%d%m%Y')
        if datetime.datetime.now()>date:
            return 'OK'
        else:
            return 'Wrong Date Code'
    except:
        return 'Wrong Date Code'

app = Flask(__name__)
@app.route("/save/<dmc>", methods=['GET'])
def savedmc(dmc):
    try:
        if len(dmc)==29:
            drc1 = dmc[9]
            drc2 = dmc[10:16]
            data = pd.read_sql(" select * FROM [DMC].[dbo].[Parameter_DMC] where Drawing_code like '%"+drc1+"%"+drc2+"%'",conn)
            Productname = data.loc[0,'ProductName']
            cursor.execute("INSERT INTO [DMC].[dbo].[DMC_Printer] (ProductName,DMC,TimeCreated,Status)VALUES (?,?,?,?)",
                Productname,
                dmc,
                datetime.datetime.now(),
                ""
            )
            conn.commit()
            return "True"
    except:
        return data
    return "False"
@app.route("/json/<dmc>", methods=['GET'])
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
            "content":"<img style='width:45px;height:45px;padding-left:30px;' src='data:image/png;base64," + imgdata + "'>"
        },
        "1":{
            "type":4,
            "content":"<img style='height:25px' src='data:images/png;base64,"+img+"'>"
        }
    }
    return jsonify(data)
@app.route("/printblank", methods=['GET'])
def printblank():
    img = cv2.imread("static/images/blank.png")
    _,img = cv2.imencode(".png",img)
    img = img.tobytes()
    img= base64.b64encode(img)
    img = img.decode('utf-8')
    data = {
        "0":{
            "type":4,
            "content":"<img style='height:14px' src='data:images/png;base64,"+img+"'>"
        }
    }
    return jsonify(data)
@app.route("/", methods=['GET'])
def hello_world():
    return render_template('html/index.html')
@app.route("/createdmc", methods=['POST'])
def creatdmc():
    castingcode=request.form['casting']
    Product=request.form['product']
    return MAQR(castingcode,Product)
@app.route("/printdmc", methods=['POST'])
def printdmc():
    dmc=request.form['dmc']
    encoder = DataMatrixEncoder(dmc).get_imagedata()
    encoded_string= base64.b64encode(encoder)
    return encoded_string.decode('utf-8')
@app.route("/decodedmc", methods=['POST'])
def decodedmc():
    #time.sleep(1000)
    global Quang
    dmc=request.form['anh'].replace(" ","+")
    imgdata = base64.b64decode(dmc)
    with open('static/result/check/test.png', 'wb') as f:
        f.write(imgdata)
    img = cv2.imread("static/result/check/test.png",0)
    # img_resized = cv2.resize(src=img, dsize=(300,300))
    # # for thresh in range(100,140,5):
    # #     ret, th = cv2.threshold(img_resized, thresh, 255, cv2.THRESH_BINARY)
    # data = pylibdmtx.decode(img_resized)
    # if len(data)>0:
    #     return str(data[0]).split("'")[1]
    # return "Can't Detect Datamatrix Code"
    # img = Image.open("static/result/check/test.png")
    msg = pylibdmtx.decode(img)
    # if len(msg)==0:
    #    Return 
    # if msg[0]!=Quang and len(msg)>0:
    #     Q=False
    # if Q==[False]:
    if len(msg)>0:
        if str(msg[0]).split("'")[1]==Quang:
            return "Trung"
        Quang=str(msg[0]).split("'")[1]
        return str(msg[0]).split("'")[1]
    # with open('static/result/ok/test'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")+'.png', 'wb') as f:
    #     f.write(imgdata)        
    else:
        for thresh in range(0,200,5):
            ret, th = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
            msg = pylibdmtx.decode(th,timeout=10)
            if len(msg)>0:
            # cv2.imwrite('static/result/ng/test'+datetime.datetime.now().strftime("%y%m%d_%H%M%S_")+str(thresh)+'.png',th)
            # with open('static/result/ng/test'+datetime.datetime.now().strftime("%y%m%d_%H%M%S_")+'thresh.png', 'wb') as f:
            #     f.write(imgdata)
                if str(msg[0]).split("'")[1]==Quang:
                    return "Trung"
                Quang=str(msg[0]).split("'")[1]
                return str(msg[0]).split("'")[1]
        # with open('static/result/ng/test'+datetime.datetime.now().strftime("%y%m%d_%H%M%S")+'.png', 'wb') as f:
        #     f.write(imgdata)
        #Quang=""
        return "Can't Detect Datamatrix Code"
if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")
