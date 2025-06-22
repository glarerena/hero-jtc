from llama_cpp import Llama  # type: ignore
from listings import get_live_housing_listings, format_listings
from application import get_housing_response
from ami_utils import handle_ami_logic
from typing import List, Optional
import re

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
        listings = get_live_housing_listings()
        return format_listings(listings)

    # 🤖 Fallback: TinyLLaMA
    try:
        prompt = (
            "### Instruction:\n"
            "You are a helpful assistant providing concise answers about affordable housing.\n\n"
            f"{format_history(history)}\n"
            "### Response:\n"
        )

        output = llm(prompt, max_tokens=128, stop=["</s>"], echo=False)
        raw = output["choices"][0]["text"].strip()

        # 🧼 Clean up any echoes of User/Assistant and [INST] noise
        cleaned = raw.replace("[INST]", "").replace("[/INST]", "").strip()
        cleaned = re.sub(r"^(User:.*?\n)?(Assistant:)?", "", cleaned, flags=re.IGNORECASE).strip()

        return cleaned

    except Exception:
        return "Sorry, I’m having trouble answering that right now."

