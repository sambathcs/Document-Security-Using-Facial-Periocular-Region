'''
		Facial Periocular Based Unique Identification
Versions:
    Python3.6
    Ubuntu14.04 (uname -a ) 





    
Used Modules:
    *dlib
     https://www.pyimagesearch.com/2018/01/22/install-dlib-easy-complete-guide/
    *imutils
     pip install imutils
    *OpenCV
     sudo apt-get install python-opencv
    *math
    *os

'''
import pyqrcode
import cv2
import os
import dlib
from imutils import face_utils
from math import sqrt
import matplotlib.pyplot as plt
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import AES

print('Initialising...')
import struct

def float_to_bin(num):
    return format(struct.unpack('!I', struct.pack('!f', num))[0], '032b')

def bin_to_float(binary):
    return struct.unpack('!f',struct.pack('!I', int(binary, 2)))[0]

def minus(p1,p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    out = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
    return out

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor
print("[INFO] loading facial landmark predictor...")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
num_setup_frames = 40
frame_count = 0
alert_count = 0
EAR_vals = []
NLR_vals = []
MOR_max = 0

filename = "SAMBATH.jpg"
print('\n[INFO] Reading file:\n\t\t',filename)
frame = cv2.imread(filename)

print('\n[INFO] Converting image to grayscale...')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

print('\n[INFO] Detecting face...')
# detect faces in the grayscale frame
rects = detector(gray, 0)
print(rects)
if len(rects) == 0:
    exit()
elif len(rects) == 1:
    rect = rects[0]
else:
    rect = rects[0]
    
    
# loop over the face detections
#for rect in rects:
# determine the facial landmarks for the face region, then
# convert the facial landmark (x, y)-coordinates to a NumPy
# array
shape1 = predictor(gray, rect)
shape1 = face_utils.shape_to_np(shape1)
print(' ')


left_eye = shape1[36:42]
right_eye = shape1[42:48]
nose = shape1[27:31]
mouth = shape1[48:60]

    
# loop over the (x, y)-coordinates for the left eye landmarks
# and draw them on the image
for (x, y) in left_eye:
        #print(x,y)
    cv2.circle(frame, (x, y), 2, (255, 0, 0), -10)

# loop over the (x, y)-coordinates for the right eye landmarks
# and draw them on the image
for (x, y) in right_eye:
        #print(x,y)
    cv2.circle(frame, (x, y), 2, (255, 0, 0), -10)

# loop over the (x, y)-coordinates for the nose landmarks
# and draw them on the image
for (x, y) in nose:
        #print(x,y)
    cv2.circle(frame, (x, y), 2, (255, 255, 0), -10)
    
# loop over the (x, y)-coordinates for the mouth landmarks
# and draw them on the image
for (x, y) in mouth:
        #print(x,y)
    cv2.circle(frame, (x, y), 2, (0, 0, 255), -10)
    

    
p = shape1
'''    
# Calculate Eye Aspect Ratio
EAR = (minus(p[37],p[41]) + minus(p[38],p[40]))/(2*minus(p[39],p[36]))
print("EAR: "+ str(EAR))  
    
 
    # Calculate MOuth Opening Ratio
MOR = (minus(p[50],p[58]) + minus(p[51],p[57]) + minus(p[52],p[56]))/(3*minus(p[54],p[48])) 
print("MOR: "+ str(MOR)+ "\t"+ str(MOR_max))

#Nose Length Ratio
nose_len = minus(p[30],p[27])
print("Nose Length: " + str(nose_len))'''


# show the frame
cv2.imshow("Frame", frame)        
key = cv2.waitKey(1000) 
cv2.destroyAllWindows()
print('\n[INFO] Detecting various features...')

inner_canthal_dist=minus(p[39],p[42])
inner_canthal_dist=round(inner_canthal_dist,3)

outer_canthal_dist=minus(p[36],p[45])
outer_canthal_dist=round(outer_canthal_dist,3)

eyelid_left=minus(p[37],p[41])
eyelid_left=round(eyelid_left,3)

upper_eyelid_left=minus(p[37],p[38])
upper_eyelid_left=round(upper_eyelid_left,3)

lower_eyelid_left=minus(p[40],p[41])
lower_eyelid_left=round(lower_eyelid_left,3)

eyelid_rightt=minus(p[47],p[43])
eyelid_rightt=round(eyelid_rightt,3)

upper_eyelid_right=minus(p[43],p[44])
upper_eyelid_right=round(upper_eyelid_right,3)

lower_eyelid_right=minus(p[46],p[47])
lower_eyelid_right=round(lower_eyelid_right,3)

left_eyebrow1=minus(p[17],p[21])
left_eyebrow1=round(left_eyebrow1,3)

left_eyebrow2=minus(p[18],p[20])
left_eyebrow2=round(left_eyebrow2,3)

left_eyebrow3=minus(p[19],p[24])
left_eyebrow3=round(left_eyebrow3,3)

right_eyebrow1=minus(p[22],p[26])
right_eyebrow1=round(right_eyebrow1,3)

right_eyebrow2=minus(p[23],p[25])
right_eyebrow2=round(right_eyebrow2)

print('\n[INFO] Concatenating features...')
mat=[inner_canthal_dist,outer_canthal_dist,eyelid_left,upper_eyelid_left,lower_eyelid_left,eyelid_rightt,upper_eyelid_right,lower_eyelid_right,left_eyebrow1,left_eyebrow2,left_eyebrow3,right_eyebrow1,right_eyebrow2] 


##random_generator = Random.new().read
##key = RSA.generate(1024, random_generator) #generate public and private keys
##
##publickey = key.publickey # pub key export for exchange
##
##encrypted = publickey.encrypt('encrypt this message', 32)
###message to encrypt is in the above line 'encrypt this message'
##
##print (encrypted )#ciphertext
##
##f = open ('encryption.txt', 'w')
##f.write(str(encrypted)) #write ciphertext to file
##f.close()
##
###decrypted code below
##
##f = open ('encryption.txt', 'r')
##message = f.read()
##
##decrypted = key.decrypt(message)
##
##print(decrypted)
##
##f = open ('encryption.txt', 'w')
##f.write(str(message))
##f.write(str(decrypted))
##f.close()

num_features = len(mat)

dat='0'
key=input('Enter AES key to encrypt \n<16 bit>')

for i in range(num_features):
    f1=str(mat[i])
    #print('encryptdata',f1)
    d=len(f1)
    #n='a'
    f=float_to_bin(float(f1))
##    A=float_bin(mat[i], places = 4)
##    print(A)
    dat=dat+f
    



# Encryption
print('\n[INFO] Performing AES Encryption...')

encryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV456')
cipher_text = encryption_suite.encrypt(bytes(dat[1:].encode()))

print('\n[INFO] Creating QR Code Image...')
import base64;
b64_string = str(base64.b64encode(cipher_text),'utf-8')
q=pyqrcode.create(b64_string)
print(q)
q.png('a.png',scale=6)


# Decryption
decryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV456')
plain_text = decryption_suite.decrypt(cipher_text)
print('decryptdata',plain_text)
##dat=dat+cipher_text

# show the QR IMAGE
cv2.imshow("QR Image", cv2.imread('a.png'))        
key = cv2.waitKey(1000) 
cv2.destroyAllWindows()







import pyzbar.pyzbar as pyzbar

image = cv2.imread("a.png")


decodedObjects = pyzbar.decode(image)
for obj in decodedObjects:
    print("Type:", obj.type)
    print("Data: ", obj.data, "\n")

cv2.imshow("Frame", image)
cv2.waitKey(10)
cv2.destroyAllWindows()
DATA=obj.data
decrypted_from_png=bytes(base64.b64decode(obj.data))


print(decrypted_from_png)
##decrypted_from_png=str(decrypted_from_png, encoding="UTF-8")
##decryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV456')
##plain_text = decryption_suite.decrypt(decrypted_from_png.decode())
##decryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV456')
##plain_text = decryption_suite.decrypt(bytes(decrypted_from_png))
##print('decryptdata',plain_text)

key=input('Enter AES key to encrypt \n<16 bit>')
decryption_suite = AES.new(key, AES.MODE_CBC, 'This is an IV456')
plain_text = decryption_suite.decrypt((decrypted_from_png))
print('decryptdata',plain_text)








