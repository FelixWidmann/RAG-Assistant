from Backend.Shared.minio_client import s3_client
from Backend.Shared.config import BUCKET_NAME

def download_from_minio(key: str):

    response = s3_client.get_object(
        Bucket=BUCKET_NAME,
        Key=key,
    )
    file_bytes = response["Body"].read()

    return file_bytes
