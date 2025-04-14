import os

def get_context(question: str) -> str:
    # Get absolute path to the context file one level up
    base_dir = os.path.dirname(os.path.abspath(__file__))  # This is python-llm-service/
    context_path = os.path.join(base_dir, "../context/affordable-housing.md")

    try:
        with open(context_path, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "⚠️ Context file not found."

