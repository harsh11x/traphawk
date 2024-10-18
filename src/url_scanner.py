import re

# List of known suspicious domains
SUSPICIOUS_DOMAINS = [
    "malicious.com", "phishing.com", "scam.com", "fake.com"
]

# List of URL shortening services
URL_SHORTENERS = [
    "bit.ly", "tinyurl.com", "goo.gl", "is.gd", "t.co"
]

def is_suspicious(url):
    """
    Check if the provided URL is suspicious.

    :param url: The URL to check.
    :return: True if the URL is suspicious, False otherwise.
    """
    # Check for suspicious domains
    for domain in SUSPICIOUS_DOMAINS:
        if domain in url:
            print(f"Warning: The URL contains a known suspicious domain: {domain}")
            return True
    
    # Check if the URL is shortened
    for shortener in URL_SHORTENERS:
        if shortener in url:
            print(f"Warning: The URL is shortened using a known URL shortener: {shortener}")
            return True

    # Check URL length
    if len(url) > 75:  # Example threshold for length
        print("Warning: The URL length is suspiciously long.")
        return True

    # Check for suspicious patterns in the URL
    if re.search(r'\b(?:login|secure|update|account)\b', url.lower()):
        print("Warning: The URL contains suspicious keywords.")
        return True

    print("This URL appears to be safe.")
    return False
