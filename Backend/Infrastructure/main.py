from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from Backend.Infrastructure.routes.chat import chat_router
from Backend.Infrastructure.routes.upload import upload_router

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:8080"
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
