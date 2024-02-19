MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
END_SCRIPT = "Finished"
ERROR_SCRIPT = "Invalid Input"
ERROR_SCRIPT_NUMBER = "Score should be 0-100 inclusive."
ERROR_SCRIPT_INTEGAR = "Invalid input, not an integer"
SCORE_SCRIPT_90 = "Excellent"
SCORE_SCRIPT_50 = "Passable"
SCORE_SCRIPT_BAD = "bad"

def main():
    score = 0
    print(MENU)
    choice = input("Enter choice: ").upper()

    while choice != "Q":
        if choice == "G":
            while score is True:
                try:
                    score = int(input("Enter score: "))
                    while score < 0 or score > 100:
                        print(ERROR_SCRIPT_NUMBER)
                        score = float(input("Enter score: "))
                    decide_message(score)
                except ValueError:
                    print(ERROR_SCRIPT_INTEGAR)
        elif choice == "P":
            result_message = decide_message(score)
            print(result_message)
        elif choice == "S":
            show_stars(score)
        else:
            print(ERROR_SCRIPT)
        print(MENU)
        choice = input("Enter choice: ").upper()

    print(END_SCRIPT)


def show_stars(score):
    print("*" * score)


def decide_message(score):
    if score >= 90:
        result_message = SCORE_SCRIPT_90
    elif score >= 50:
        result_message = SCORE_SCRIPT_50
    else:
        result_message = SCORE_SCRIPT_BAD
    return result_message

main()