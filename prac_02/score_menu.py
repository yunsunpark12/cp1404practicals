MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
END_SCRIPT = "Farewell"
ERROR_SCRIPT = "Invalid Input"
ERROR_SCRIPT_NUMBER = "Score should be 0-100 inclusive."
INVALID_SCORE_MINIMUM = 0
INVALID_SCORE_MAXIMUM = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50
SCORE_VOID_SCRIPT = "Enter score first"

def main():
    """Show menu, get score, determine message, and show stars"""
    score = 0
    print(MENU)
    choice = input("Enter choice: ").upper()

    while choice != "Q":            # while choice is not Q, keep asking user's menu choice

        if choice == "G":
            score = get_score()
        elif choice == "P":
            score = check_score_existence(score)
            result_message = determine_message(score)
            print(result_message)
        elif choice == "S":
            score = check_score_existence(score)
            show_stars(score)
        else:
            print(ERROR_SCRIPT)
        print(MENU)
        choice = input("Enter choice: ").upper()

    print(END_SCRIPT)


def check_score_existence(score):
    """check if score is void"""
    while score <= 0:
        print(SCORE_VOID_SCRIPT)
        score = get_score()
    return score

def get_score():
    "Get user score and validate"
    score = int(input("Enter score: "))
    while score < INVALID_SCORE_MINIMUM or score > INVALID_SCORE_MAXIMUM:  # error check to make sure score is 0-100 inclusive
        print(ERROR_SCRIPT_NUMBER)
        score = int(input("Enter score: "))
    return score


def show_stars(score):
    """Print asterisks as much as the score"""
    print("*" * score)


def determine_message(score):
    """Show appropriate message for user's score"""
    if score >= EXCELLENT_SCORE:
        result_message = "Excellent"
    elif score >= PASSABLE_SCORE:
        result_message = "Passable"
    else:
        result_message = "Bad"
    return result_message

main()
