from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rag_utils import get_context

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/generate") 
async def generate_response(request: Request):
    data = await request.json()
    message = data.get("message", "")

    print("📩 Received from NestJS:", message)

    # Get context using your RAG logic
    context = get_context(message)

    if context:
        print(f"✅ Context generated (length: {len(context)} chars)")
    else:
        print("⚠️ No context generated or listings found.")

    return { "response": context }

