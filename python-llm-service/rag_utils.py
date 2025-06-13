from llama_cpp import Llama  # type: ignore
from listings import get_live_housing_listings, format_listings
from application import get_housing_response
from ami_utils import handle_ami_logic
from typing import List, Optional

# Load model once
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

    # 💰 AMI logic
    ami_keywords = ['income', 'ami', 'make', 'earn', 'salary', 'how much']
    if any(keyword in question for keyword in ami_keywords):
        try:
            return handle_ami_logic(question)
        except:
            return "I'm sorry, I couldn't process your income question."

    # 📝 Application logic
    if "apply" in question or "application" in question:
        return get_housing_response(question)

    # 🏘️ Listings logic
    if "listings" in question or "available" in question or "show" in question:
        listings = get_live_housing_listings()
        return format_listings(listings)

    # 🤖 Fallback to LLM with multi-turn context
    try:
        prompt = f"[INST] You are a helpful assistant providing concise, focused answers about affordable housing. Keep responses brief and to the point.\n\n{format_history(history)}User: {question}\nAssistant: [/INST]"
        output = llm(prompt, max_tokens=128, stop=["</s>"], echo=False)
        return output["choices"][0]["text"].strip()
    except Exception as e:
        return "Sorry, I'm having trouble generating a response right now."
