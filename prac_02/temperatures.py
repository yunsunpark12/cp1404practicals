MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit"
ERROR_SCRIPT = "Invalid option"
END_SCRIPT = "Thank you."

def main():
    """Show menu, convert Celsius to Fahrenheit and vice versa"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":        # while choice is not Q, keep accepting menu choice
        if choice == "C":
            get_fahrenheit()

        elif choice == "F":
            get_celsius()

        else:
            print(ERROR_SCRIPT)
        print(MENU)
        choice = input(">>> ").upper()
    print(END_SCRIPT)


def get_celsius():
    """Calculate fahrenheit into celsius"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} degrees C")


def get_fahrenheit():
    """Calculate celsius into fahrenheit"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


main()