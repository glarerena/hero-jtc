from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rag_utils import get_context
from typing import List, Optional
from pydantic import BaseModel

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[Message]] = []

app = FastAPI(
    title="HERO Python API", 
    description="Affordable Housing Assistant API",
    docs_url=None,  # Disable Swagger UI
    redoc_url=None  # Disable ReDoc
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    """Health check endpoint for Render"""
    return {"status": "healthy", "service": "HERO Python API"}

@app.post("/generate") 
async def generate_response(request: ChatRequest):
    message = request.message
    history = request.history

    print("📩 Received from NestJS:", message)
    print("📜 Conversation history:", history)

    # Get context using your RAG logic, now with conversation history
    context = get_context(message, history)

    if context:
        print(f"✅ Context generated (length: {len(context)} chars)")
    else:
        print("⚠️ No context generated or listings found.")

    return { "response": context }

@app.get("/{path:path}")
async def catch_all(path: str):
    """Catch all route to help debug 404s"""
    return {"error": "Not found", "path": path, "available_endpoints": ["/", "/health", "/api/health", "/status", "/generate"]}

