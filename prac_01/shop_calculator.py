""""
A shop requires a small program that would allow them to quickly work out the total price for a number of items, each with different prices.

The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.

The output should look something like (bold text represents user input):

Number of items: 3
Price of item: 100
Price of item: 35.56
Price of item: 3.24
Total price for 3 items is $124.92

get number_of_items
get price_of_item
if total_price > 100
    final_price = total_price * 0.9
else
    final_price = total_price
print final_price
"""

number_items = int(input("Number of items:"))
while number_items < 0:
    for i in range(number_items):
        prices = float(input("Price of item:"))
    total = += prices
    if total > 100:
        final = total * 0.9
    elif total <= 100:
        final = total
    else:
        print("Invalid")
    print(f"Total price for {number_items} items is ${final}")
print("Invalid Input")
number_items = int(input("Number of items:"))