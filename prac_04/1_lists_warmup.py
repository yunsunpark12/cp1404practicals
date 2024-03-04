numbers = ["ten", 1, 4, 1, 5, 9, 1]
"""
numbers[0]      # 3
numbers[-1]     # 2
numbers[3]      # 1
numbers[:-1]    # 9, 5, 1, 4, 1, 3 
numbers[3:4]    # 1, 5
5 in numbers    # True
7 in numbers    # False
"3" in numbers  # False
numbers + [6, 5, 3] # [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
"""

"""
Print all the elements from numbers except the first two (slice)
numbers[2:]

Print whether 9 is an element of numbers
9 in numbers
"""