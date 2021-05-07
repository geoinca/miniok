# Necessary imports
import cv2,boto3
import numpy as np
#from google.colab.patches import cv2_imshow
import sys,os
from os import scandir, getcwd
from os.path import abspath

from botocore.client import Config



def ls(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]

def read_file(filename):
  img = cv2.imread(filename)
  #cv2_imshow(img)
  return img

def color_quantization(img, k):
# Transform the image
  data = np.float32(img).reshape((-1, 3))

# Determine criteria
  criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 0.001)

# Implementing K-Means
  ret, label, center = cv2.kmeans(data, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
  center = np.uint8(center)
  result = center[label.flatten()]
  result = result.reshape(img.shape)
  return result


def edge_mask(img, line_size, blur_value):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray_blur = cv2.medianBlur(gray, blur_value)
  edges = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, line_size, blur_value)
  return edges

def check(s3AccessKey,s3SecretKey,s3EndPointUrl,s3Bucket,s3BucketOut,s3OutFileName,s3Prefix):
  s3 = boto3.resource('s3',
                      endpoint_url=s3EndPointUrl,
                      aws_access_key_id=s3AccessKey,
                      aws_secret_access_key=s3SecretKey,
                      config=Config(signature_version='s3v4'),
                      region_name='us-east-1')

  mnt_loc = os.getcwd()+"/tmp/"

  my_bucket = s3.Bucket(s3Bucket)
  s3_files = []
  for object in my_bucket.objects.filter(Prefix=s3Prefix):
    path, filename = os.path.split(object.key)
    my_bucket.download_file(object.key, mnt_loc +filename)

  imgWarp=ls(mnt_loc)
  img = cv2.imread(imgWarp[0])
  line_size = 7
  blur_value = 7
  edges = edge_mask(img, line_size, blur_value)
  #cv2_imshow(edges)
  total_color = 9
  img = color_quantization(img, total_color)

  blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200,sigmaSpace=200)
  cartoon = cv2.bitwise_and(blurred, blurred, mask=edges)

  #cv2_imshow(rotated)
  imgResult=mnt_loc+"10cartoon0000.jpeg"
  cv2.imwrite(imgResult, cartoon)
  imgout=s3Prefix + s3OutFileName

  s3.Bucket(s3BucketOut).upload_file(imgResult,imgout)
  s3_client = boto3.client('s3',
                      endpoint_url=s3EndPointUrl,
                      aws_access_key_id=s3AccessKey,
                      aws_secret_access_key=s3SecretKey,
                      config=Config(signature_version='s3v4'),
                      region_name='us-east-1')
  response = s3_client.list_objects_v2(Bucket=s3Bucket, Prefix=s3Prefix)

  for object in response['Contents']:
      print('Deleting', object['Key'])
      s3_client.delete_object(Bucket=s3Bucket, Key=object['Key'])

if __name__ == '__main__':
    if len(sys.argv) != 4:
        s3AccessKey = sys.argv[1]
        s3SecretKey = sys.argv[2]
        s3EndPointUrl= sys.argv[3]
        s3Bucket= sys.argv[4]
        s3BucketOut= sys.argv[5]
        s3OutFileName= sys.argv[6]
        s3Prefix=sys.argv[7]
        check(s3AccessKey,s3SecretKey,s3EndPointUrl,s3Bucket,s3BucketOut,s3OutFileName,s3Prefix)
    else:
        print (0)

s3AccessKey = 'AKIAIOSFODNN7EXAMPLE'
s3SecretKey = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
s3EndPointUrl = 'http://argo-artifacts:9000'
s3Bucket='input'
s3BucketOut='output'
s3OutFileName="imgresult0000.jpeg"
s3Prefix="id1/"