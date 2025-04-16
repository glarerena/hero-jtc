import os
import requests


# def get_context(question: str) -> str:
#     # Get absolute path to the context file one level up
#     base_dir = os.path.dirname(os.path.abspath(__file__))  # This is python-llm-service/
#     context_path = os.path.join(base_dir, "../context/affordable-housing.md")

#     try:
#         with open(context_path, "r") as f:
#             return f.read()
#     except FileNotFoundError:
#         return "⚠️ Context file not found."

def get_context(question: str) -> str:
    listings = get_live_housing_listings()
    if not listings:
        return "⚠️ No housing listings available at the moment."
    
    formatted_listings = []
    for item in listings:
        title = item.get("title", "No Title")
        link = item.get("application_link", "#")
        location = item.get("location", "Unknown location")
        description = item.get("description", "No description available")
        
        # Format each listing as a markdown bullet point or block
        formatted_listing = (
            f"**[{title}]({link})**\n"
            f"Location: {location}\n"
            f"Description: {description}\n"
        )
        formatted_listings.append(formatted_listing)
    
    return "\n".join(formatted_listings)

def get_live_housing_listings():
    # Update this base URL to match your API deployment
    base_url = "http://localhost:3000"
    # The relative route defined in the controller, using a query to filter for the SF Bay Area
    endpoint = "/listings?location=San%20Francisco%20Bay%20Area"
    url = f"{base_url}{endpoint}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an exception for HTTP errors
        listings = response.json()     # Convert the JSON response to a Python object (list/dict)
        return listings
    except requests.RequestException as e:
        # Log the error (or print) and return an empty list or error message
        print(f"Error fetching dynamic housing data: {e}")
        return []
