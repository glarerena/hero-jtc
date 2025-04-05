from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import os

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding

# 🧠 Set Ollama model
Settings.llm = Ollama(model="mistral", request_timeout=120)
Settings.embed_model = OllamaEmbedding(model_name="mistral")

# 📄 Load and index documents once when server starts
documents = SimpleDirectoryReader("../data", recursive=True).load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()


app = FastAPI()

# 🔓 Allow access from frontend (optional for dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🌐 Route for serving the web form


@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

# 📩 Handle query submissions from the frontend form


@app.post("/query")
async def query_rag(payload: dict):
    question = payload.get("query", "")

    if not question:
        return {"response": "No question provided."}

    response = query_engine.query(question)
    return {"response": response.response}
