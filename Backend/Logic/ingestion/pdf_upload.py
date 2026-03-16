from fastapi import UploadFile
from fastapi.responses import JSONResponse
from Backend.Shared.minio_client import s3_client
from Backend.Shared.config import BUCKET_NAME

async def upload_pdf(file: UploadFile):

    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are allowed"}

    # Read file content in memory
    contents = await file.read()
    key = file.filename

    # Upload to MinIO
    response = s3_client.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=contents
    )

    code = response["ResponseMetadata"]["HTTPStatusCode"]

    if code == 200:
        return JSONResponse({"filename": file.filename, "status": "uploaded successfully", "status_code": code})
    else:
        return JSONResponse({"filename": file.filename, "status": "uploaded failed", "status_code": code})