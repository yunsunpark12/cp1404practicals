TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator")
tariff_choice = input("which tariff? 11 or 31: ")
kWh_price = int(input("Enter cents per kWh:"))
daily_use = float(input("Enter daily use in kWh:"))
no_of_days = int(input("Enter number of billing days:"))


if tariff_choice == 11:
    tariff = TARIFF_11
else:
    tariff = TARIFF_31

total_bill = tariff * kWh_price * daily_use * no_of_days
print(f"Estimated bill: $ {total_bill:.2f}")