import whois
from datetime import datetime

def get_domain_age(domain):
    """
    Get the age of the domain in years.

    Args:
        domain (str): The domain name to check.

    Returns:
        int: Age of the domain in years, or None if the domain is not registered.
    """
    try:
        domain_info = whois.whois(domain)
        creation_date = domain_info.creation_date

        if isinstance(creation_date, list):
            # If the creation_date is a list, take the first one
            creation_date = creation_date[0]

        if creation_date:
            age = datetime.now() - creation_date
            return age.days // 365  # Convert days to years
        else:
            return None
    except Exception as e:
        print(f"Error retrieving domain information: {e}")
        return None

def is_domain_suspicious(domain):
    """
    Determine if a domain is suspicious based on its age.

    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain is suspicious (age < 1 year), False otherwise.
    """
    age = get_domain_age(domain)
    if age is not None:
        return age < 1  # Consider domains younger than 1 year as suspicious
    return False
