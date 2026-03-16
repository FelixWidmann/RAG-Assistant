# backend/routes/chat.py
from fastapi import APIRouter
from pydantic import BaseModel

chat_router = APIRouter()

#define query class
class ChatRequest(BaseModel):
    question: str

#define answer Class
class ChatResponse(BaseModel):
    answer: str

@chat_router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    answer = "test" #await orchestrate_query(request.question) #Aufruf der in orchestrator.py definierten RAG Pipeline
    return ChatResponse(answer=answer)

@chat_router.post("/ask", response_model=ChatResponse)
def chat_answer(request: ChatRequest):
    answer = f'you asked: {request.question}' #Aufruf der in orchestrator.py definierten RAG Pipeline
    return ChatResponse(answer=answer)