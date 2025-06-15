import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

listings_data = [
    {
        "name": "401 Market St – 2BR, San Francisco",
        "link": "https://bloom.exygy.dev/listing/d699ceb2-f59c-4459-85e2-5a649915ecfe/testing_design_lottery_copy_401_market_street_san_francisco_ca"
    },
    {
        "name": "434 Bennington Ct – 1BR, Saline MI",
        "link": "https://bloom.exygy.dev/listing/2d805d18-1586-4eef-b6e0-da3612c88951/lottery_demo_434_bennington_ct_saline_mi"
    },
    {
        "name": "64 Grinnell Dr – 3BR, West Glacier MT",
        "link": "https://bloom.exygy.dev/listing/16815545-3a1a-4639-b2e9-94206a16ba6a/district_demo_copy_64_grinnell_dr_west_glacier_mt"
    },
    {
        "name": "1233 W Main – Studios, Chicago IL",
        "link": "https://bloom.exygy.dev/listing/cf908bad-5e0d-41ce-b688-f4be27408449/test_another_lottery_1233_w_main_chicago_il"
    },
    {
        "name": "Emily Apartments – 64 Grinnell Dr, MT",
        "link": "https://bloom.exygy.dev/listing/ca935750-769d-4062-a0b7-d52005c3aa74/testing_design_emily_64_grinnell_dr_west_glacier_mt"
    }
]

def get_live_housing_listings() -> list:
    """
    Returns the full listing list (if needed elsewhere)
    """
    return listings_data

def format_listings(listings: list) -> str:
    """
    Returns only one random formatted listing per call.
    """
    if not listings:
        return "⚠️ No housing listings available at the moment."

    listing = random.choice(listings)
    return f"🏠 **[{listing['name']}]({listing['link']})**"
