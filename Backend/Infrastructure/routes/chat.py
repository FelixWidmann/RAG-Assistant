# backend/routes/chat.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from Backend.Infrastructure.orchestrator import orchestrate_query

class QuestionRequest(BaseModel):
    question: str
    collection: str

chat_router = APIRouter()

@chat_router.post("/ask")
def chat_answer(request: QuestionRequest):
    
    query = request.question
    collection = request.collection

    #run retrieval pipeline
    try:
    
        answer = orchestrate_query(query, collection)

        return JSONResponse({"answer": answer })
    
    except Exception as e:

        raise HTTPException(status_code=500, detail= str(e))
