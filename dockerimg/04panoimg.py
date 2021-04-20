
import os, sys
import boto3
import cv2

from os import scandir, getcwd
from os.path import abspath

import numpy as np
import datetime
from botocore.client import Config

def ls(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]

def check(s3AccessKey,s3SecretAccessKey,s3EndPointUrl,s3Bucket,s3BucketOut,s3OutFileName):
    s3 = boto3.resource('s3',
                        endpoint_url=s3EndPointUrl,
                        aws_access_key_id=s3AccessKey,
                        aws_secret_access_key=s3SecretAccessKey,
                        config=Config(signature_version='s3v4'),
                        region_name='us-east-1')

    mnt_loc = os.getcwd()+"/tmp/"
    my_bucket = s3.Bucket(s3Bucket)
    s3_files = []
    for object in my_bucket.objects.all():
        s3_files.append(object)

    for elem in s3_files:
        s3.Bucket(elem.bucket_name).download_file(elem.key, mnt_loc + elem.key)

    imgWarp=ls(mnt_loc)

    new_imgs = []
    for item in imgWarp:
        img = cv2.imread(item)
        new_imgs.append(img)

    stitcher = cv2.Stitcher.create(cv2.Stitcher_PANORAMA)
    status, pano = stitcher.stitch(new_imgs)

    if status != cv2.Stitcher_OK:
        print("Can't stitch images, error code = %d" % status)
        sys.exit(-1)

    imgResult=mnt_loc+"imgpano.jpeg"
    cv2.imwrite(imgResult, pano)

    s3.Bucket(s3BucketOut).upload_file(imgResult,s3OutFileName)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        s3AccesKey = sys.argv[1]
        s3SecretKey = sys.argv[2]
        s3EndPointUrl= sys.argv[3]
        s3Bucket= sys.argv[4]
        s3BucketOut= sys.argv[5]
        s3OutFileName= sys.argv[6]
        check(s3AccesKey,s3SecretKey,s3EndPointUrl,s3Bucket,s3BucketOut,s3OutFileName)
    else:
        print (0)


 
s3AccesKey = 'tfq0M5o1QtNOJcP1nizr'
s3SecretKey = 'HbO5COQOXR6z3P0jgTVCBzWxkXFPXKsMqoItRzL6'
s3EndPointUrl = 'http://argo-artifacts:9000'
s3Bucket='infolder'
s3BucketOut='outfolder'
s3OutFileName="pano0000.jpeg"