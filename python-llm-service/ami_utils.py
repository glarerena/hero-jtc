def handle_ami_logic(question: str) -> str:
    """
    Parses the user's income and provides AMI-based guidance.

    Edge cases handled:
      1. Empty or missing input
      2. Non-numeric input
      3. Decimal values (rounded to nearest integer)
      4. Zero or negative incomes (invalid)
    """
    #This is only for 1 person household
    #https://www.hcd.ca.gov/sites/default/files/docs/grants-and-funding/income-limits-2024.pdf
    #using San Francisco County AMI numbers for 2024 since DAHLIA project is in San Francisco
    #AMI = 
    # acutely low: 19600
    # extremely low: 41150
    # very low income: 68550
    # low income: 109700
    # median income: 130600
    # moderate income 156750

    print("🔢 Processing AMI question:", question)  # Debug log

    # 1) Check for empty or None
    if not question or not question.strip():
        return "Please enter your household income."

    # 2) Extract the number from the question
    import re
    # Look for numbers in the text, including those with commas and decimal points
    numbers = re.findall(r'\$?\d+(?:,\d+)*(?:\.\d+)?', question)
    if not numbers:
        return "Sorry, I couldn't find an income amount in your question. Please include a specific number."
    
    # Take the first number found
    cleaned = numbers[0].replace(",", "").lstrip("$")
    print("🧹 Cleaned input:", cleaned)  # Debug log

    # 3) Try parsing as float (to handle decimals), then convert to int
    try:
        income_float = float(cleaned)
        print("✅ Parsed income:", income_float)  # Debug log
    except ValueError:
        return "Sorry, I couldn't understand that income amount."

    # 4) Reject zero or negative incomes
    if income_float <= 0:
        return "Income must be a positive number."

    # Round to nearest dollar
    income = int(round(income_float))
    print("💰 Final income value:", income)  # Debug log

    # 5) Check against the ordered thresholds
    if income < 19_600:
        return "You are in the acutely low AMI group (≤20% AMI)."
    elif income < 41_150:
        return "You are in the extremely low AMI group (≤30% AMI)."
    elif income < 68_550:
        return "You are in the very low AMI group (≤50% AMI)."
    elif income < 109_700:
        return "You are in the low AMI group (≤80% AMI)."
    elif income < 130_600:
        return "You are in the median AMI group (≤100% AMI)."
    elif income < 156_750:
        return "You are in the moderate AMI group (≤120% AMI)."
    else:
        return "You are above the moderate AMI group (>120% AMI)."


    
        

