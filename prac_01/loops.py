#a
for i in range(0, 101, 10):
    print(i, end=' ')
print()

#b
for i in range(20, 0, -1):
    print(i, end=' ')
print()

#c
number = int(input("Number of Stars:"))
for i in range(number):
    print("*", end=' ')
print()

#d
num_rows = int(input("Number of rows"));
k = 1
for i in range(0, num_rows):
    for j in range(0, k):
        print("* ", end="")
    k = k + 1
    print()