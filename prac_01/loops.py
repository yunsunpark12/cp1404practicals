#a
for i in range(0, 100, 10):
    print(i, end='')
print()

#b
for i in range(20,0):
    print(i, end='')
print()

#c
number = int(input("Enter number: "))
print("*" * number)

#d
number = int(input("Enter number: "))
for i in range(1,number+1):
    print(i* "*", end='')
    print()