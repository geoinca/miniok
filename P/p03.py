#pip install opencv-contrib-python
# numpy
import sys,os
from os import scandir, getcwd
from os.path import abspath
import cv2
import numpy as np
import datetime

def ls(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]

nPhoto=6
n = 0
imgs = []
while(n < nPhoto):
    archivo = "tmp/img"+str(n)+".jpeg"
    print(archivo)
    img = cv2.imread(archivo)
    imgs.append(img)
    n += 1

mnt_loc = os.getcwd()+"/tmp/"
imgWarp=ls(mnt_loc)


#Stitch the images on the array, and save the output image. 
stitcher = cv2.Stitcher.create(cv2.Stitcher_PANORAMA)
status, pano = stitcher.stitch(imgs)

if status != cv2.Stitcher_OK:
    print("Can't stitch images, error code = %d" % status)
    sys.exit(-1)

cv2.imwrite("resultado.jpeg", pano)