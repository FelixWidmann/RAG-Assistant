from fastapi import FastAPI
from pydantic import BaseModel
from contextlib import asynccontextmanager
import requests
from fastapi.middleware.cors import CORSMiddleware
from Backend.Infrastructure.routes.chat import chat_router
from Backend.Infrastructure.routes.upload import upload_router
from Backend.Infrastructure.routes.projects import project_router
from Backend.Logic.retrieval.generation import warmup_ollama


#Call Ollama on application startup to run Model and keep it in memory for faster response time.
@asynccontextmanager
async def lifespan(app: FastAPI):
    warmup_response = warmup_ollama()
    print(f"Warmup finished: {warmup_response}")
    yield


app = FastAPI(lifespan=lifespan)

origins = [
    "http://localhost:5173",
    "http://localhost:8080",
    "http://frontend:80",
    "http://localhost:80",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Router for handling the chat response
app.include_router(chat_router)
app.include_router(upload_router)
app.include_router(project_router)
