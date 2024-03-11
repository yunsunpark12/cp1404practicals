"""
Estimate: 40 minutes
Actual:    minutes
"""


def main():
    email_to_name = {}
    email = input("Email: ")        # lindsay.ward@jcu.edu.au
    while email != '':
        email_split_a = email.split('@')[0]
        email_split_name = email_split_a.split('.')
        name = email_split_name


        user_answer = input(f"Is your name {name}? (Y/n)").lower()
        if user_answer == "n":
        # get rid of number
        else:
    # display user name
    for  # iterate dic
        print(f"{# name} ({#email})")


main()