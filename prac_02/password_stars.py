PASSWORD_LENGTH = 10
ERROR_MESSAGE = "Password should be at least 10 characters."

def main():
    password = get_password()
    print_asterisks(password)


def get_password():
    """get user password, error check so that is meets the minimum password length"""
    password = input("Enter password: ")
    while len(password) < PASSWORD_LENGTH:
        print(ERROR_MESSAGE)
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """print asterisks as long as the word"""
    print("*" * len(password))

main()