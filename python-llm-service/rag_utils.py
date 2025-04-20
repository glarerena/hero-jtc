import requests
import json

def get_context(question: str) -> str:
    listings = get_live_housing_listings()
    if not listings:
        return "⚠️ No housing listings available at the moment."
    
    formatted_listings = []
    for item in listings:
        if not isinstance(item, dict):
            continue

        # Extract essential fields
        title = item.get("name", "No Title")
        
        # Extract location (jurisdiction name)
        jurisdiction = item.get("jurisdictions", {})
        location = jurisdiction.get("name", "Unknown location") if isinstance(jurisdiction, dict) else "Unknown location"
        
        # Add fallback for missing descriptions
        description = item.get("description") or "No description available"
        
        # Construct clickable link using urlSlug
        slug = item.get("urlSlug", "")
        link = f"https://bloom.exygy.dev/listing/{slug}" if slug else "#"
        
        # Final listing format
        formatted_listing = (
            f"**[{title}]({link})**\n"
            f"Location: {location}\n"
            f"Description: {description}\n"
        )
        formatted_listings.append(formatted_listing)
    
    return "\n".join(formatted_listings)


def get_live_housing_listings():
    base_url = "http://localhost:3100"
    endpoint = "/listings?limit=5"
    url = f"{base_url}{endpoint}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        # Handle response structure
        if isinstance(data, dict):
            return data.get("items", data.get("data", []))
        return data

    except (requests.RequestException, json.JSONDecodeError) as e:
        print(f"❌ Error fetching housing data: {e}")
        return []


# Run as standalone script for testing
if __name__ == "__main__":
    print(get_context("Show me listings"))
