def get_application_info() -> str:
    """
    Returns information about the housing application process.
    """
    return "To apply for housing, please visit our application portal at https://bloom.exygy.dev/applications/start/choose-language?listingId=ca935750-769d-4062-a0b7-d52005c3aa74"

def format_application_response() -> str:
    """
    Formats the application response with the application link.
    """
    application_info = get_application_info()
    # Convert the plain URL to a Markdown link
    application_info = application_info.replace(
        "https://bloom.exygy.dev/applications/start/choose-language?listingId=ca935750-769d-4062-a0b7-d52005c3aa74",
        "[Apply for Housing](https://bloom.exygy.dev/applications/start/choose-language?listingId=ca935750-769d-4062-a0b7-d52005c3aa74)"
    )
    return f"🏠 {application_info}\n\nPlease note that you'll need to have your documents ready when applying. For listing and application questions, please contact the Leasing Agent displayed on the listing."

def is_housing_related(question: str) -> bool:
    """
    Checks if the question is related to housing.
    """
    housing_keywords = ["listings", "listing", "housing", "housing", "apartments", "apartment", "rentals", "rental", "home", "property", "properties", "houses", "rent"]
    return any(keyword in question.lower() for keyword in housing_keywords)

def get_housing_response(question: str) -> str:
    """
    Returns the appropriate response for housing-related queries.
    """
    if "apply" in question.lower() or "application" in question.lower():
        return format_application_response()
    return "I can help you find housing options. Would you like to see available listings or learn about the application process?" 