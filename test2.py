import pandas as pd
import pyodbc
import datetime
conn = pyodbc.connect(
            'Driver={SQL Server}; Server=WIN-1SJHDOU69JS; ;Database=DMC;uid=sa; pwd=P@ssw0rd; Trusted_Connection=No;')
cursor = conn.cursor()
def MAQR(Malo,Productname):
    #if malo_str(Malo) != "OK":
        #return malo_str(Malo)
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
    Qrcode=str(serial)+Mabanve+Maphienban+MaSX+Makhuonsap+Malo[:7]+xulynhiet
    #if len(Qrcode) != 29:
        #return 'Wrong Quantity DMC'
    cursor.execute("INSERT INTO [DMC].[dbo].[DMC_Printer] (ProductName,DMC,TimeCreated,Status)VALUES (?,?,?,?)",
        Productname,
        Qrcode.upper(),
        datetime.datetime.now(),
        "Fixed DMC"
    )
    conn.commit()
    cursor.execute("Update [DMC].[dbo].[Parameter_DMC] Set Parameter_setting = '"+str(int(serial)+1)+"' Where ProductName='"+Productname+"'" )
    cursor.commit()
    return Qrcode.upper()
print(MAQR("2x22x222","A2012004"))
