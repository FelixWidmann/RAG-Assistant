import boto3
from botocore.client import Config
from Backend.Shared.config import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY

s3_client = boto3.client(
    "s3",
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY,
    config=Config(signature_version="s3v4"),
)

def ensure_bucket():
    buckets = [b["Name"] for b in s3_client.list_buckets()["Buckets"]]
    if BUCKET_NAME not in buckets:
        s3_client.create_bucket(Bucket=BUCKET_NAME)