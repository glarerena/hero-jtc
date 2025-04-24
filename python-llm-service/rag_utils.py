import requests
import random

def get_context(question: str) -> str:
    listings = get_live_housing_listings()
    if not listings:
        return "⚠️ No housing listings available at the moment."
    
    random.shuffle(listings)
    selected_listings = listings[:5]

    # All links will go here when clicked
    fixed_redirect_link = "https://bloom.exygy.dev/listing/f3ba0555-e9fa-4f12-a1a1-d11a8c82293d/test_listing_399_blossom_hill_san_jose_ca"

    formatted_listings = []
    for item in selected_listings:
        if not isinstance(item, dict):
            continue

        title = item.get("name", "No Title")
        jurisdiction = item.get("jurisdictions", {})
        location = jurisdiction.get("name", "Unknown location") if isinstance(jurisdiction, dict) else "Unknown location"

        formatted_listing = (
            f"**[{title}]({fixed_redirect_link})**\n"
            f"Location: {location}\n"
        )
        formatted_listings.append(formatted_listing)

    return "\n".join(formatted_listings)


def get_live_housing_listings():
    base_url = "http://localhost:3100"
    endpoint = "/listings?limit=5"
    url = f"{base_url}{endpoint}"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, dict):
            return data.get("items", data.get("data", []))
        return data

    except requests.RequestException as e:
        print(f"❌ Error fetching housing data: {e}")
        return []

# For local testing
if __name__ == "__main__":
    print(get_context("show me listings"))
