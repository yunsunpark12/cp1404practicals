MENU_SCRIPT = "1. Show the even numbers from x to y\n2. Show the odd numbers from x to y\n3. Show the squares of the numbers from x to y (e.g., if x, y = 2, 4 then: 4 9 16)\n4. Exit the program"
QUIT_MESSAGE = "Finished."
EVEN_NUMBER_SCRIPT = ""

number_x = int(input("Enter a number for x: "))
number_y = int(input("Enter a number for y: "))

"""
if x % 2 = 0:   # x is an even number
    for i in range(x,y+1,2)
else:
    for i in range(x+1,y+1,2)
"""

print(MENU_SCRIPT)