"""
emails
Estimate: 25 minutes
Actual:   28 minutes
"""
def main():
    """Get email and name then print them."""
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation != "" and confirmation != "y":
            name = input("Name: ").strip()
        email_to_name[email] = name
        email = input("Email: ").strip()
    for email_key, name_value in email_to_name.items():
        print(f"{name_value} ({email_key})")

def extract_name(email):
    """Extract name from email."""
    return email[:email.index("@")].replace(".", " ").title()




main()