#pip install opencv-contrib-python
# numpy
import sys,os
import cv2
import numpy as np
import datetime

#Read each of the images and then put it in the array
def getFileName():
    datetime_object = datetime.datetime.now()
    print(datetime_object)
    d1 = str(datetime_object)
    output = d1.replace(":","")
    output = output.replace(" ","_")
    output = output[0:17]+".jpg"
    return output

nPhoto=3
n = 0
imgs = []
while(n < nPhoto):
    archivo = "tmp/resultado0"+str(n)+".jpeg"
    print(archivo)
    img = cv2.imread(archivo)
    imgs.append(img)
    n += 1

#Stitch the images on the array, and save the output image. 
stitcher = cv2.Stitcher.create(cv2.Stitcher_PANORAMA)
status, pano = stitcher.stitch(imgs)

if status != cv2.Stitcher_OK:
    print("Can't stitch images, error code = %d" % status)
    sys.exit(-1)

cv2.imwrite("resultado.jpeg", pano)