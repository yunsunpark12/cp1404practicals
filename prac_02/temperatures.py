MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
ERROR_SCRIPT = "Invalid option"
END_SCRIPT = "Thank you."

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":        # while choice is not Q, keep accepting menu choice
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = calculate_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")

        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = calculate_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} degrees C")

        else:
            print(ERROR_SCRIPT)
        print(MENU)
        choice = input(">>> ").upper()
    print(END_SCRIPT)

# turn fahrenheit into celsius
def calculate_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

# turn celsius into fahrenheit
def calculate_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()