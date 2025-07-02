from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rag_utils import get_context
from typing import List, Optional
from pydantic import BaseModel

# -----------------------------
# Models
# -----------------------------

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    history: Optional[List[Message]] = []

# -----------------------------
# FastAPI Setup
# -----------------------------

app = FastAPI(
    title="HERO Python API",
    description="Affordable Housing Assistant API",
    docs_url=None,   # Disable Swagger UI
    redoc_url=None   # Disable ReDoc
)

# -----------------------------
# CORS Middleware
# -----------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",               # Local development
        "https://hero-app.vercel.app",         # Vercel deployment
        "https://first-hero.dev"      # ✅ Replace after domain purchase
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"]
)

# -----------------------------
# Routes
# -----------------------------

@app.get("/")
async def root():
    """Health check endpoint for Render"""
    return {"status": "healthy", "service": "HERO Python API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "HERO Python API is running"}

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

    return {"response": context}

@app.get("/{path:path}")
async def catch_all(path: str):
    return {"message": f"You reached {path}. The server is running!"}
