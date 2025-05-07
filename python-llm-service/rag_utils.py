# rag_utils.py

from listings import get_live_housing_listings, format_listings

def get_context(question: str) -> str:
    """
    Processes the user's question and returns the appropriate response.
    """
    question = question.lower().strip()

    # Respond to listing requests
    if "listings" in question:
        listings = get_live_housing_listings()
        return format_listings(listings)

    # Default response for unrecognized questions
    return "I'm sorry, I didn't understand your request. Please try again."

# For local testing
if __name__ == "__main__":
    print(get_context("show me listings"))

