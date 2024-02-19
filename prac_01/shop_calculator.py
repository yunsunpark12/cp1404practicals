DC_START_PRICE = 100
DISCOUNT_RATE = 0.90

total_item_price = 0
number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price = float(input("Price of item: "))

    while price < 0:
        print("Invalid input!")
        price = float(input("Price of item: "))

    total_item_price += price

if total_item_price > DC_START_PRICE:
    total_item_price *= DISCOUNT_RATE  # apply 10% discount

print(f"Total price for {number_of_items} items is ${total_item_price:.2f}")