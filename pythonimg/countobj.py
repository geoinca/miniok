import boto3
from botocore.client import Config

S3_ACCESS_KEY = 'tfq0M5o1QtNOJcP1nizr'
S3_SECRET_KEY = 'HbO5COQOXR6z3P0jgTVCBzWxkXFPXKsMqoItRzL6'

s3 = boto3.resource('s3',
                    endpoint_url='http://argo-artifacts:9000',
                    aws_access_key_id='tfq0M5o1QtNOJcP1nizr',
                    aws_secret_access_key='HbO5COQOXR6z3P0jgTVCBzWxkXFPXKsMqoItRzL6',
                    config=Config(signature_version='s3v4'),
                    region_name='us-east-1')

my_bucket = s3.Bucket('infolder')
countObj=0
for object_summary in my_bucket.objects.filter(Prefix=""):
    countObj+=1
   
print (countObj)