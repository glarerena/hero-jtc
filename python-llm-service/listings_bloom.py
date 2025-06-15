import requests
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_live_housing_listings() -> list:
    """
    Fetches the 5 available housing listings from Bloom's API.
    This endpoint is known to return a fixed set of 5 listings.
    """
    base_url = "http://localhost:3100"
    endpoint = "/listings"
    url = f"{base_url}{endpoint}"

    try:
        logging.info(f"Fetching the 5 available listings from: {url}")
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        if isinstance(data, dict):
            listings = data.get("items", data.get("data", []))
            if listings:
                logging.info(f"Successfully fetched the 5 available listings from {url}")
                return listings
            else:
                logging.warning(f"Endpoint {url} returned empty list.")
                return []  # Return an empty list to indicate no data
        else:
            logging.warning(f"Unexpected response format from {url}: {data}")
            return [] # Return empty list

    except requests.RequestException as e:
        logging.error(f"Error fetching housing data from {url}: {e}")
        return []  # Return empty list
    
def format_listings(listings: list) -> str:
    """
    Formats the listings for display in the chatbot.
    """
    if not listings:
        return "⚠️ No housing listings available at the moment."
    
    random.shuffle(listings)
    selected_listings = listings[:5]

    # Redirect link updated to your specified link
    fixed_redirect_link = "https://bloom.exygy.dev/listing/d699ceb2-f59c-4459-85e2-5a649915ecfe/testing_design_lottery_copy_401_market_street_san_francisco_ca"
    formatted_listings = []

    for item in selected_listings:
        if not isinstance(item, dict):
            continue

        title = item.get("name", "No Title")
        
        formatted_listing = (
            f"**[{title}]({fixed_redirect_link})**\n"
        )
        formatted_listings.append(formatted_listing)

    return "\n".join(formatted_listings)

