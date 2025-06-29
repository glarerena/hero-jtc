from listings import get_live_housing_listings, format_listings
from application import get_housing_response
from ami_utils import handle_ami_logic
from typing import List, Optional
import re
import os

# Load context once at startup
def load_housing_context():
    try:
        context_path = os.path.join(os.path.dirname(__file__), "..", "context", "affordable-housing.md")
        with open(context_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except Exception as e:
        print(f"⚠️ Could not load context file: {e}")
        return ""

HOUSING_CONTEXT = load_housing_context()

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

    # 💰 AMI
    if "ami" in question or "income" in question or "how much" in question:
        return handle_ami_logic(30000)  # simulate a test income case

    # 📝 Application
    if "apply" in question or "application" in question:
        return get_housing_response(question)

    # 🏘️ Listings
    if "listings" in question or "available" in question or "housing" in question:
        listings = get_live_housing_listings()
        return format_listings(listings)

    # 🏠 General housing questions
    if any(word in question for word in ["housing", "affordable", "rent", "program", "help", "resource"]):
        return """🏠 **Affordable Housing Resources in the Bay Area**

Here are the key resources and programs available:

**📚 Key Resources:**
- [San Francisco Housing Portal](https://housing.sfgov.org) - Official affordable housing listings and lottery applications
- [Alameda County Affordable Housing](https://www.acgov.org/cda/hcd/housing/affordablehousing.htm) - County programs and rental assistance resources  
- [California Housing Finance Agency (CalHFA)](https://www.calhfa.ca.gov) - Statewide help for renters, homeowners, and first-time buyers

**🏠 Common Programs:**
- **Section 8 Vouchers** – Helps low-income renters pay private-market rent
- **Public Housing** – Government-managed housing for eligible individuals and families
- **BMR Units (San Francisco)** – Discounted rents for qualifying applicants
- **Local Housing Authorities** – City/county rental help and navigation programs

**✅ Basic Eligibility Criteria:**
- Income (usually ≤ 50–80% of AMI)
- Household size
- Legal status (citizen or eligible immigration)
- Rental history

Would you like me to show you current available listings or help with applications?"""

    # 📋 Documents and requirements
    if any(word in question for word in ["document", "paperwork", "need", "require", "bring"]):
        return """📄 **Documents You'll Need to Gather:**

**Essential Documents:**
- Photo ID
- Social Security cards
- Proof of income (pay stubs, tax returns)
- Lease or address proof (utility bills, letters)
- Immigration docs (if applicable)
- Landlord references

**📌 Application Tips:**
- Apply to multiple waitlists
- Keep contact info updated
- Respond promptly to notifications
- Ask for accommodations if needed
- Use local housing counselors when possible

Need help with the application process?"""

    # 🤖 Fallback: General help response
    return """👋 **Welcome to HERO - Your Bay Area Housing Assistant!**

I can help you with:
- 🏠 **Available housing listings** - Ask for "listings" or "available housing"
- 📝 **Application help** - Ask about "applications" or "how to apply"
- 💰 **Income requirements** - Ask about "AMI" or "income limits"
- 📄 **Required documents** - Ask about "documents" or "paperwork"
- 🏘️ **General housing resources** - Ask about "resources" or "programs"

What would you like to know about affordable housing in the Bay Area?"""

