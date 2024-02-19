import random

ERROR_SCRIPT = "Invalid score"
INVALID_SCORE_1 = 0
INVALID_SCORE_2 = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50

def main():
    """Get user score, determine message, and show result message."""
    score = float(input("Enter score: "))
    result_message = determine_message(score)
    print(result_message)

    # print random score and result of it
    random_score = random.randint(0,101)
    print("Random score: ", random_score)
    result_random_message = determine_message(random_score)
    print("Result for random score: ", result_random_message)


def determine_message(score):
    """Show appropriate message for user's score"""
    if score < INVALID_SCORE_1 or score > INVALID_SCORE_2:
        result_message = ERROR_SCRIPT
    elif score >= EXCELLENT_SCORE:
        result_message = "Excellent"
    elif score >= PASSABLE_SCORE:
        result_message = "Passable"
    else:
        result_message = "Bad"
    return result_message

main()