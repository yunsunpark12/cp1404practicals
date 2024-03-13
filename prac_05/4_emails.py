"""
Estimate: 40 minutes
Actual:   30 minutes
"""

def main():
    """Get email dictionary to names and user confirmation """
    email_to_name = {}
    email = input("Email: ")        # e.g.  lindsay.ward@jcu.edu.au
    while email != '':
        name = get_name_from_email(email)
        user_confirmation = input(f"Is your name {name}? (Y/n)").lower()
        if user_confirmation == "y" or user_confirmation == ' ':
            # store both name & email to dictionary
            email_to_name[email] = name
        else:
            name = input("Name: ")
            email_to_name[email] = name

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Get names from user email"""
    email_splitted_by_a = email.split('@')[0]
    name_in_email = email_splitted_by_a.split('.')
    name =''.join(name_in_email).title()
    return name


main()