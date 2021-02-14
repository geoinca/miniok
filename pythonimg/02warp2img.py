import sys,os
from os import scandir, getcwd
from os.path import abspath
import cv2
import numpy as np
import boto3
from botocore.client import Config

def ls(ruta = getcwd()):
    return [abspath(arch.path) for arch in scandir(ruta) if arch.is_file()]

#from google.colab.patches import cv2_imshow
def draw_matches(img1, keypoints1, img2, keypoints2, matches):
  r, c = img1.shape[:2]
  r1, c1 = img2.shape[:2]

  # Create a blank image with the size of the first image + second image
  output_img = np.zeros((max([r, r1]), c+c1, 3), dtype='uint8')
  output_img[:r, :c, :] = np.dstack([img1, img1, img1])
  output_img[:r1, c:c+c1, :] = np.dstack([img2, img2, img2])

  # Go over all of the matching points and extract them
  for match in matches:
    img1_idx = match.queryIdx
    img2_idx = match.trainIdx
    (x1, y1) = keypoints1[img1_idx].pt
    (x2, y2) = keypoints2[img2_idx].pt

    # Draw circles on the keypoints
    cv2.circle(output_img, (int(x1),int(y1)), 4, (0, 255, 255), 1)
    cv2.circle(output_img, (int(x2)+c,int(y2)), 4, (0, 255, 255), 1)

    # Connect the same keypoints
    cv2.line(output_img, (int(x1),int(y1)), (int(x2)+c,int(y2)), (0, 255, 255), 1)
    
  return output_img

def warpImages(img1, img2, H):

  rows1, cols1 = img1.shape[:2]
  rows2, cols2 = img2.shape[:2]

  list_of_points_1 = np.float32([[0,0], [0, rows1],[cols1, rows1], [cols1, 0]]).reshape(-1, 1, 2)
  temp_points = np.float32([[0,0], [0,rows2], [cols2,rows2], [cols2,0]]).reshape(-1,1,2)

  # When we have established a homography we need to warp perspective
  # Change field of view
  list_of_points_2 = cv2.perspectiveTransform(temp_points, H)

  list_of_points = np.concatenate((list_of_points_1,list_of_points_2), axis=0)

  [x_min, y_min] = np.int32(list_of_points.min(axis=0).ravel() - 0.5)
  [x_max, y_max] = np.int32(list_of_points.max(axis=0).ravel() + 0.5)
  
  translation_dist = [-x_min,-y_min]
  
  H_translation = np.array([[1, 0, translation_dist[0]], [0, 1, translation_dist[1]], [0, 0, 1]])

  output_img = cv2.warpPerspective(img2, H_translation.dot(H), (x_max-x_min, y_max-y_min))
  output_img[translation_dist[1]:rows1+translation_dist[1], translation_dist[0]:cols1+translation_dist[0]] = img1

  return output_img

def check(s3AccessKey,s3SecretAccessKey,s3EndPointUrl,s3Bucket,s3BucketOut):

  s3 = boto3.resource('s3',
                      endpoint_url=s3EndPointUrl,
                      aws_access_key_id=s3AccesKey,
                      aws_secret_access_key=s3SecretKey,
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
  imgResult=mnt_loc+"imgresult01.jpeg"
  img1 = cv2.imread(imgWarp[0])
  img2 = cv2.imread(imgWarp[1])

  img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

  orb = cv2.ORB_create(nfeatures=2000)

  # Find the key points and descriptors with ORB
  keypoints1, descriptors1 = orb.detectAndCompute(img1, None)
  keypoints2, descriptors2 = orb.detectAndCompute(img2, None)
  # Create a BFMatcher object.
  # It will find all of the matching keypoints on two images
  bf = cv2.BFMatcher_create(cv2.NORM_HAMMING)

  # Find matching points
  matches = bf.knnMatch(descriptors1, descriptors2,k=2)
  #print(keypoints1[0].pt)
  #print(keypoints1[0].size)
  #print("Descriptor of the first keypoint: ")
  #print(descriptors1[0])

  all_matches = []
  for m, n in matches:
    all_matches.append(m)

  img3 = draw_matches(img1_gray, keypoints1, img2_gray, keypoints2, all_matches[:30])

  good = []
  for m, n in matches:
      if m.distance < 0.6 * n.distance:
          good.append(m)
      
  cv2.drawKeypoints(img1, [keypoints1[m.queryIdx] for m in good], None, (255, 0, 255))

  MIN_MATCH_COUNT = 5

  if len(good) > MIN_MATCH_COUNT:
      # Convert keypoints to an argument for findHomography
      src_pts = np.float32([ keypoints1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
      dst_pts = np.float32([ keypoints2[m.trainIdx].pt for m in good]).reshape(-1,1,2)

      # Establish a homography
      M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
      
      result = warpImages(img2, img1, M)
      cv2.imwrite(imgResult, result)

  s3.Bucket(s3BucketOut).upload_file(imgResult,'imgresult01.jpeg')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        s3AccesKey = sys.argv[1]
        s3SecretKey = sys.argv[2]
        s3EndPointUrl= sys.argv[3]
        s3Bucket= sys.argv[4]
        s3BucketOut= sys.argv[5]
        check(s3AccesKey,s3SecretKey,s3EndPointUrl,s3Bucket,s3BucketOut)
    else:
        print (0)

s3AccesKey = 'tfq0M5o1QtNOJcP1nizr'
s3SecretKey = 'HbO5COQOXR6z3P0jgTVCBzWxkXFPXKsMqoItRzL6'
s3EndPointUrl = 'http://argo-artifacts:9000'
s3Bucket='infolder'
s3BucketOut='outfolder'

