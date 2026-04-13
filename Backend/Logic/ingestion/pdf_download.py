from Backend.Shared.minio_client import s3_client
from Backend.Shared.config import MINIO_BUCKET_NAME

def download_from_minio(key: str):

    try:
        
        response = s3_client.get_object(
        Bucket=MINIO_BUCKET_NAME,
        Key=key,
        )

        file_bytes = response["Body"].read()

        return file_bytes
    
    except Exception as e: 
        
        raise RuntimeError(f"Failed to retrieve File") from e
