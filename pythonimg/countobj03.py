import sys,os
import cv2
import numpy as np
import boto3
from botocore.client import Config

s3AccesKey = 'tfq0M5o1QtNOJcP1nizr'
s3SecretKey = 'HbO5COQOXR6z3P0jgTVCBzWxkXFPXKsMqoItRzL6'
s3EndPointUrl = 'http://argo-artifacts:9000'
s3Bucket='infolder'

s3 = boto3.resource('s3',
                    endpoint_url=s3EndPointUrl,
                    aws_access_key_id=s3AccesKey,
                    aws_secret_access_key=s3SecretKey,
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

mnt_loc = os.getcwd()+"/tmp"
print(mnt_loc)

my_bucket = s3.Bucket(s3Bucket)
s3_files = []
for object in my_bucket.objects.all():
    s3_files.append(object)

for elem in s3_files:
    s3.Bucket(elem.bucket_name).download_file(elem.key, mnt_loc + elem.key)
    print (elem.key)