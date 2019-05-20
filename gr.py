import pyqrcode 
from pyqrcode import QRCode 
import os
import cv2
  
# String which represent the QR code 
s = "www.geeksforgeeks.org fdjkrnftr joijel kpoop[ ekrklp;[ l[pwqelr [pl[p r "
  
# Generate QR code 
url = pyqrcode.create(s) 
h=os.getcwd()
# Create and save the png file naming "myqr.png" 
url.svg("myqr.svg", scale = 8) 
from  tkinter import *
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir =h,title = "choose your file",filetypes = (("jpeg files","*.svg"),("all files","*.*")))
print (root.filename)
root.withdraw()


import pyzbar.pyzbar as pyzbar

image = cv2.imread(root.filename )


decodedObjects = pyzbar.decode(root.filename )
for obj in decodedObjects:
    print("Type:", obj.type)
    print("Data: ", obj.data, "\n")

cv2.imshow("Frame", image)
cv2.waitKey(10)
cv2.destroyAllWindows()
DATA=obj.data
decrypted_from_png=bytes(base64.b64decode(obj.data))


print(decrypted_from_png)
