import os, sys
import boto3
from botocore.client import Config

         
def check(s3AccessKey,s3SecretAccessKey,s3EndPointUrl,s3Bucket,s3BucketOut,s3OutFileName,s3Prefix):
    s3 = boto3.resource('s3',
                        endpoint_url=s3EndPointUrl,
                        aws_access_key_id=s3AccessKey,
                        aws_secret_access_key=s3SecretAccessKey,
                        config=Config(signature_version='s3v4'),
                        region_name='us-east-1')

    my_bucket = s3.Bucket(s3Bucket)
    result=0
    for object_summary in my_bucket.objects.filter(Prefix=s3Prefix):
        result+=1

    print (result)
    if result>2:
        result=3
    a = ["doNothing", "faceAlignment", "warpImages", "panorama"]
    f = open("/tmp/tfmresult.txt", "w")

    f.write(a[result])
    f.close()

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


s3AccessKey = 'tfq0M5o1QtNOJcP1nizr'
s3SecretKey = 'HbO5COQOXR6z3P0jgTVCBzWxkXFPXKsMqoItRzL6'
s3EndPointUrl = 'http://argo-artifacts:9000'
s3Bucket='infolder'
s3BucketOut='outfolder'
s3OutFileName="imgresult0000.jpeg"
s3Prefix="id1/"
 
