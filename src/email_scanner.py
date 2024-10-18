import re

# List of common phishing keywords
PHISHING_KEYWORDS = [
    "urgent", "act now", "confirm your account", "verify your account",
    "reset your password", "click here", "free", "winner", "prize",
    "limited time", "account suspended", "sensitive information"
]

def analyze_email(email_content):
    """
    Analyze the provided email content for potential phishing attempts.

    :param email_content: The content of the email to analyze.
    :return: None
    """
    # Check for phishing keywords
    suspicious_keywords = [keyword for keyword in PHISHING_KEYWORDS if keyword in email_content.lower()]
    
    if suspicious_keywords:
        print(f"Warning: This email contains suspicious keywords: {', '.join(suspicious_keywords)}")
    else:
        print("This email appears to be safe based on keyword analysis.")

    # Check for suspicious links (basic example)
    links = re.findall(r'http[s]?://[^\s]+', email_content)
    if links:
        print("Links found in the email:")
        for link in links:
            print(f" - {link}")
    else:
        print("No links found in the email.")
