from llama_cpp import Llama  # type: ignore
from listings import get_live_housing_listings, format_listings
from application import get_housing_response
from ami_utils import handle_ami_logic
from typing import List, Optional

# Load TinyLLaMA once
llm = Llama(model_path="models/tinyllama.gguf", n_ctx=2048)

class Message:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

def format_history(history: List[Message]) -> str:
    chat = ""
    for msg in history:
        role = "User" if msg.role == "user" else "Assistant"
        chat += f"{role}: {msg.content.strip()}\n"
    return chat

def get_context(question: str, history: Optional[List[Message]] = None) -> str:
    question = question.lower().strip()
    history = history or []

    # 💰 AMI
    if "ami" in question or "income" in question or "how much" in question:
        return handle_ami_logic(30000)  # simulate a test income case

    # 📝 Application
    if "apply" in question or "application" in question:
        return get_housing_response(question)

    # 🏘️ Listings
    if "listings" in question or "available" in question:
        listings = get_live_housing_listings()  # this should be hardcoded now
        return format_listings(listings)

    # 🤖 Fallback: TinyLLaMA
    try:
        prompt = f"[INST] You are a helpful assistant providing concise, focused answers about affordable housing.\n\n{format_history(history)}User: {question}\nAssistant: [/INST]"
        output = llm(prompt, max_tokens=128, stop=["</s>"], echo=False)
        return output["choices"][0]["text"].strip()
    except Exception:
        return "Sorry, I’m having trouble answering that right now."
