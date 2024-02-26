"""
Q1. Write code that asks the user for their name,
then opens a file called "6_name.txt" and writes that name to it.
Remember to close your file.
"""

FILENAME = "6_name.txt"
out_file = open(FILENAME, 'w')
name = input("What is your name? ")
print(name, file = out_file)
out_file.close()