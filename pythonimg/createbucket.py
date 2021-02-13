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

s3.create_bucket(Bucket='artifacts', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
s3.create_bucket(Bucket='infolder', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
s3.create_bucket(Bucket='outfolder', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})

my_bucket = s3.Bucket(s3Bucket)
countObj=0
for object_summary in my_bucket.objects.filter(Prefix=""):
    countObj+=1
   
print (countObj)

