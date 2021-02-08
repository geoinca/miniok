
import os, sys
import boto3
from botocore.client import Config


def check(s3AccessKey,s3SecretAccessKey,s3EndPointUrl,s3Bucket):
    s3 = boto3.resource('s3',
                        endpoint_url=s3EndPointUrl,
                        aws_access_key_id=s3AccessKey,
                        aws_secret_access_key=s3SecretAccessKey,
                        config=Config(signature_version='s3v4'),
                        region_name='us-east-1')

    my_bucket = s3.Bucket(s3Bucket)
    countObj=0
    for object_summary in my_bucket.objects.filter(Prefix=""):
        countObj+=1
    
    print (countObj)


if __name__ == '__main__':
    if len(sys.argv) != 4:
        s3AccesKey = sys.argv[1]
        s3SecretKey = sys.argv[2]
        s3EndPointUrl= sys.argv[3]
        s3Bucket= sys.argv[4]
        check(s3AccesKey,s3SecretKey,s3EndPointUrl,s3Bucket)
    else:
        print (0)







s3EndPointURL='http://argo-artifacts:9000'
s3AccessKey='tfq0M5o1QtNOJcP1nizr'
s3SecretAccessKey='HbO5COQOXR6z3P0jgTVCBzWxkXFPXKsMqoItRzL6'
s3Bucket='infolder'

 
