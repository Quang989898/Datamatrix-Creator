from PIL import Image
from pylibdmtx import pylibdmtx
img = Image.open("test.png")
msg = pylibdmtx.decode(img)
if len(msg)>0:
    print(str(msg[0]).split("'")[1])
else:
    print(msg)
