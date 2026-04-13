from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from Backend.Shared.minio_client import s3_client
from Backend.Infrastructure.orchestrator import orchestrate_ingestion
from Backend.Logic.ingestion.pdf_upload import upload_pdf

upload_router = APIRouter()

@upload_router.post("/upload")
async def upload_embed_book(
    file: UploadFile = File(...),
    collection: str = Form(...)
):
    try:
        #upload document to minio
        response = await upload_pdf(file)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail=str(response))

        key = file.filename

        #run Ingestion Pipeline
        message = orchestrate_ingestion(key, collection)

        return JSONResponse({"filename": file.filename,"status": f"{message}"})

    except Exception as e: 

        print(str(e))
        
        raise HTTPException(status_code=500, detail = str(e))
