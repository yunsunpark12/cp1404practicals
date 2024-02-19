"""
On paper, write a program that asks the user for a password,
with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
The program should then print asterisks as long as the word.
Example: if the user enters Pythonista (10 characters), the program should print **********.

It's a valuable skill to be able to write code with pen and paper --
without the support of an IDE. Watch out for things like
consistent variable names and clear indenting as well as basic syntax like colons and brackets.
"""

PASSWORD_LENGTH = 10
ERROR_MESSAGE = "Password should be longer than 9 charcters."

password = input("Enter password: ")
while len(password) < PASSWORD_LENGTH:
    print(ERROR_MESSAGE)
    password = input("Enter password: ")
print("*" * len(password))