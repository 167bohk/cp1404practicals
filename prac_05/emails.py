"""
emails
Estimate: 25 minutes
Actual:    minutes
"""
def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()
        if confirmation != "" and confirmation != "y":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ")
    for email_key, name_value in email_to_name.items():
        print(f"{name_value} ({email_key})")
def extract_name():
    pass




main()