# rag_utils.py

from listings import get_live_housing_listings, format_listings
from application import get_housing_response
from ami_utils import handle_ami_logic
from typing import List, Optional

class Message:
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

def get_context(question: str, history: Optional[List[Message]] = None) -> str:
    """
    Processes the user's question and returns the appropriate response.
    Takes into account conversation history for context-aware responses.
    """
    question = question.lower().strip()
    history = history or []
    
    print("🔍 Processing question:", question)  # Debug log

    # Check for AMI-related questions first
    ami_keywords = ['income', 'ami', 'make', 'earn', 'salary', 'how much', 'earn']
    if any(keyword in question for keyword in ami_keywords):
        print("💰 Detected AMI-related question")  # Debug log
        try:
            response = handle_ami_logic(question)
            print("✅ AMI response:", response)  # Debug log
            return response
        except Exception as e:
            print("❌ Error in AMI handling:", str(e))  # Debug log
            return f"I'm sorry, I had trouble processing your income question. Please try again with a specific amount."

    # Check if this is a follow-up question about applications
    if history and any("apply" in msg.content.lower() or "application" in msg.content.lower() for msg in history):
        if "how" in question or "what" in question or "where" in question:
            return get_housing_response(question)

    # Check for application-related queries first
    if "apply" in question or "application" in question:
        return get_housing_response(question)

    # Check if this is a follow-up question about listings
    if history and any("listings" in msg.content.lower() for msg in history):
        if "more" in question or "another" in question or "other" in question:
            listings = get_live_housing_listings()
            return format_listings(listings)

    # Respond to listing requests
    if "listings" in question or "show" in question or "available" in question:
        listings = get_live_housing_listings()
        return format_listings(listings)

    # Default response for unrecognized questions
    return "I'm sorry, I didn't understand your request. Please try again."

# For local testing
if __name__ == "__main__":
    test_questions = [
        "What's my AMI with $45,000?",
        "I make $75,000",
        "My income is $120,000"
    ]
    for q in test_questions:
        print(f"\nTesting question: {q}")
        print(get_context(q))

