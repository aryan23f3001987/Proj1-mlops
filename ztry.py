import boto3
import os

s3 = boto3.resource(
    "s3",
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    region_name="us-east-1"
)

bucket = s3.Bucket("my-model-mlopsproj-03")

print("All objects in bucket:")
for obj in bucket.objects.all():
    print(obj.key)
