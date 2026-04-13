from fastapi import UploadFile
from fastapi.responses import JSONResponse
from Backend.Shared.minio_client import s3_client
from Backend.Shared.config import MINIO_BUCKET_NAME

async def upload_pdf(file: UploadFile):

    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are allowed"}

    # Read file content in memory
    contents = await file.read()
    key = file.filename

    try: 
        # Upload to MinIO
        response = s3_client.put_object(
            Bucket=MINIO_BUCKET_NAME,
            Key=key,
            Body=contents
        )

        code = response["ResponseMetadata"]["HTTPStatusCode"]

        return JSONResponse({"filename": file.filename, "status": "uploaded successfully", "status_code": code})
    
    except Exception as e: 
        
        raise RuntimeError(f"Failed to upload File") from e