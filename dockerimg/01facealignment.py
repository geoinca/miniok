# Necessary imports
import cv2,boto3
import numpy as np
#from google.colab.patches import cv2_imshow
import sys,os
from os import scandir, getcwd
from os.path import abspath
import cv2
import numpy as np
import boto3
from botocore.client import Config



def ls(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]

def check(s3AccessKey,s3SecretAccessKey,s3EndPointUrl,s3Bucket,s3BucketOut,s3OutFileName):

  s3 = boto3.resource('s3',
                      endpoint_url=s3EndPointUrl,
                      aws_access_key_id=s3AccesKey,
                      aws_secret_access_key=s3SecretKey,
                      config=Config(signature_version='s3v4'),
                      region_name='us-east-1')

  mnt_loc = os.getcwd()+"/tmp/"
  print(mnt_loc)

  my_bucket = s3.Bucket(s3Bucket)
  s3_files = []
  for object in my_bucket.objects.all():
      s3_files.append(object)

  for elem in s3_files:
      s3.Bucket(elem.bucket_name).download_file(elem.key, mnt_loc + elem.key)


  # Creating face_cascade and eye_cascade objects
  face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
  eye_cascade=cv2.CascadeClassifier("haarcascade_eye.xml")

  imgWarp=ls(mnt_loc)
  img = cv2.imread(imgWarp[0])
  #cv2_imshow(img)

  # Converting the image into grayscale
  gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  # Creating variable faces
  faces= face_cascade.detectMultiScale (gray, 1.1, 4)
  # Defining and drawing the rectangle around the face
  for(x , y,  w,  h) in faces:
    cv2.rectangle(img, (x,y) ,(x+w, y+h), (0,255,0), 3)
  #cv2_imshow(img)


  # Creating two regions of interests3OutFileName
  roi_gray=gray[y:(y+h), x:(x+w)]
  roi_color=img[y:(y+h), x:(x+w)]

  # Creating variable eyes
  eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)
  index=0
  # Creating for loop in order to divide one eye from another
  for (ex , ey,  ew,  eh) in eyes:
    if index == 0:
      eye_1 = (ex, ey, ew, eh)
    elif index == 1:
      eye_2 = (ex, ey, ew, eh)
  # Drawing rectangles around the eyes
    cv2.rectangle(roi_color, (ex,ey) ,(ex+ew, ey+eh), (0,0,255), 3)
    index = index + 1
  #cv2_imshow(img)

  if eye_1[0] < eye_2[0]:
    left_eye = eye_1
    right_eye = eye_2
  else:
    left_eye = eye_2
    right_eye = eye_1

  # Calculating coordinates of a central points of the rectangles
  left_eye_center = (int(left_eye[0] + (left_eye[2] / 2)), int(left_eye[1] + (left_eye[3] / 2)))
  left_eye_x = left_eye_center[0] 
  left_eye_y = left_eye_center[1]
  
  right_eye_center = (int(right_eye[0] + (right_eye[2]/2)), int(right_eye[1] + (right_eye[3]/2)))
  right_eye_x = right_eye_center[0]
  right_eye_y = right_eye_center[1]
  
  cv2.circle(roi_color, left_eye_center, 5, (255, 0, 0) , -1)
  cv2.circle(roi_color, right_eye_center, 5, (255, 0, 0) , -1)
  cv2.line(roi_color,right_eye_center, left_eye_center,(0,200,200),3)

  if left_eye_y > right_eye_y:
    A = (right_eye_x, left_eye_y)
    # Integer -1 indicates that the image will rotate in the clockwise direction
    direction = -1 
  else:
    A = (left_eye_x, right_eye_y)
    # Integer 1 indicates that image will rotate in the counter clockwise  
    # direction
    direction = 1 

  cv2.circle(roi_color, A, 5, (255, 0, 0) , -1)
  
  cv2.line(roi_color,right_eye_center, left_eye_center,(0,200,200),3)
  cv2.line(roi_color,left_eye_center, A,(0,200,200),3)
  cv2.line(roi_color,right_eye_center, A,(0,200,200),3)
  #cv2_imshow(img)

  delta_x = right_eye_x - left_eye_x
  delta_y = right_eye_y - left_eye_y
  angle=np.arctan(delta_y/delta_x)
  angle = (angle * 180) / np.pi


  h, w = img.shape[:2]
  # Calculating a center point of the image
  # Integer division "//"" ensures that we receive whole numbers
  center = (w // 2, h // 2)
  # Defining a matrix M and calling
  # cv2.getRotationMatrix2D method
  M = cv2.getRotationMatrix2D(center, (angle), 1.0)
  # Applying the rotation to our image using the
  # cv2.warpAffine method
  rotated = cv2.warpAffine(img, M, (w, h))
  #cv2_imshow(rotated)
  imgResult=mnt_loc+"imgresult0000.jpeg"
  cv2.imwrite(imgResult, rotated)


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
s3OutFileName="imgresult0000.jpeg"