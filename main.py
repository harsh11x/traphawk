from src.url_scanner import is_suspicious  # Assuming you have this function
from src.email_scanner import analyze_email  # Assuming you have this function
from src.domain_checker import get_domain_age, is_domain_suspicious

# ANSI escape codes for coloring
GREEN = "\033[92m"    # Green text
BLUE = "\033[94m"     # Blue text
WHITE = "\033[97m"    # White text
RESET = "\033[0m"     # Reset to default color

def main():
    print("\n\n") 
    print(f"{GREEN}TrapHawk developed by Harsh Dev{RESET}\n")
    print(f"{GREEN}Github: harsh11x{RESET}\n\n")
    print(f"{BLUE}Select your option! \n")
    print("1. Scan a URL")
    print("2. Analyze an email")
    print("3. Check a domain age")
    print(f"{RESET}")
    
    choice = input("Select an option: ")

    if choice == '1':
        url = input("Enter the URL to scan: ")
        if is_suspicious(url):
            print(f"{WHITE}Warning: This URL is suspicious!{RESET}")
        else:
            print(f"{WHITE}This URL appears to be safe.{RESET}")

    elif choice == '2':
        email_content = input("Enter the email content to analyze: ")
        # Call the email analysis function (make sure it's implemented)
        analyze_email(email_content)

    elif choice == '3':
        domain = input("Enter the domain to check (e.g., example.com): ")
        age = get_domain_age(domain)
        if age is not None:
            print(f"{WHITE}The domain {domain} is {age} years old.{RESET}")
            if is_domain_suspicious(domain):
                print(f"{WHITE}Warning: This domain is considered suspicious!{RESET}")
            else:
                print(f"{WHITE}This domain appears to be safe.{RESET}")
        else:
            print(f"{WHITE}Domain information could not be retrieved.{RESET}")

    else:
        print(f"{WHITE}Invalid choice!{RESET}")

if __name__ == "__main__":
    main()
