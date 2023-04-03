"""
Refactor password check program to use functions

Yunsun Park 13980787
20.03.2023

get password
while length of password is smaller than 8
    display "Make the password longer than 8 characters"
    get password
print "*" * length of password
"""
def main():
    password = get_password()
    length = len(password)
    print(print_star())

def get_password():
    password = input("Create password: ")
    while len(password) < 8:
        print("Make the password longer than 8 characters")
        password = input("Create password: ")

def print_star():
    print("*" * len(password))

main()

