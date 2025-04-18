from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from rag_utils import get_context

app = FastAPI()

# Optional CORS for dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate_response(request: Request):
    data = await request.json()
    message = data.get("message", "")
    
    # Get relevant context (live housing listings)
    context = get_context(message)

    # ✅ Return full response, no truncation
    return {
        "response": context
    }

