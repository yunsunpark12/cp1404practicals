"""
Yunsun Park
20.03.2023
"""
def get_score():
    while True:
        try:
            score = int(input("Enter a score between 0 and 100 inclusive: "))
            if score < 0 or score > 100:
                print("Score must be between 0 and 100 inclusive.")
            else:
                return score
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def print_result(score):
    result = "Pass" if score >= 60 else "Fail"
    print(f"The result is: {result}")

def show_stars(score):
    print("*" * score)

def main():
    score = get_score()
    while True:
        print("Main Menu")
        print("---------")
        print("G)et a valid score")
        print("P)rint result")
        print("S)how stars")
        print("Q)uit")
        choice = input("Enter your choice: ").upper()
        if choice == "G":
            score = get_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell!")

main()
