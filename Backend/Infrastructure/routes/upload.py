from fastapi import APIRouter, UploadFile
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from Backend.Shared.minio_client import s3_client
from Backend.Shared.config import BUCKET_NAME
from Backend.Infrastructure.orchestrator import orchestrate_ingestion
from Backend.Logic.ingestion.pdf_upload import upload_pdf


upload_router = APIRouter()

@upload_router.post("/upload")
async def upload_embed_book(file: UploadFile):
    
    response = await upload_pdf(file)

    key = file.filename

    if response.status_code == 200:
        
        success, message = orchestrate_ingestion(key)

        if success:

            return JSONResponse({"filename": file.filename, "status": message})
        else:
            return JSONResponse({"filename": file.filename, "status": message})

    else: 
        
        return response
