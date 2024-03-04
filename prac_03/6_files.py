"""
Q1. Write code that asks the user for their name,
then opens a file called "6_name.txt" and writes that name to it.
Remember to close your file.
"""

# name = input("What is your name? ")
# FILENAME = "6_name.txt"
# out_file = open(FILENAME, 'w')
# print(name, file = out_file)
# out_file.close()

"""
Q2. (In the same file, but as if it were a separate program)
Write code that opens "name.txt" and reads the name (as above) then prints,
"Your name is Bob" (or whatever the name is in the file).
"""

# FILENAME = "6_name.txt"
# in_file = open(FILENAME, 'r')
# name = in_file.read().strip()
# in_file.close()
# print("Your name is", name)

"""
Q3. Create a text file called numbers.txt and save it in your prac directory. 
Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens "numbers.txt", reads only the first two numbers 
and adds them together then prints the result, which should be... 59.
"""

# FILENAME = "6_numbers.txt"
# in_file = open(FILENAME, 'r')
# number_1 = int(in_file.readline())
# number_2 = int(in_file.readline())
# in_file.close()
# print("Result: ", number_1 + number_2)

FILENAME = "6_numbers.txt"
total = 0
in_file = open(FILENAME, 'r')
for i in range(0,2):
    number = int(in_file.readline())
    total += number
in_file.close()
print("Result: ", total)
"""
Q4. Now write a fourth block of code that prints 
the total for all lines in numbers.txt or a file with any number of numbers.
"""

# FILENAME = "6_numbers.txt"
# total = 0
# in_file = open(FILENAME, 'r')
# for line in in_file:
#    number = int(line)
#    total += number
# in_file.close()
# print("Result: ", total)
