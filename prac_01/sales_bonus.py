"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

get sales
while sales >= 0
    calculate bonus
    get sales
do next thing
"""

LOW_SALES = 0.10
HIGH_SALES = 0.15

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales >= 1000:
        bonus = sales * HIGH_SALES
    elif sales < 1000:
        bonus = sales * LOW_SALES
    print("Your bonus is $",bonus)
    sales = float(input("Enter sales: $"))
print("Wrong input")
