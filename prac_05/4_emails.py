"""
Estimate: 40 minutes
Actual:    minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")        # e.g.  lindsay.ward@jcu.edu.au
    while email != '':
        name = get_name_from_email(email)
        user_confirmation = input(f"Is your name {name}? (Y/n)").lower()
        if user_confirmation == "n":
        # get rid of number
        else:
    # display user name
    for  # iterate dic
        print(f"{# name} ({#email})")


def get_name_from_email(email):
    email_splitted_by_a = email.split('@')[0]
    name_in_email = email_splitted_by_a.split('.')
    name =.join(name_in_email).title()
    return name


main()