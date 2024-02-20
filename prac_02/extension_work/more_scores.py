import random

ERROR_SCRIPT = "Invalid input"
END_SCRIPT = "Finished"
INVALID_SCORE_MINIMUM = 0
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50

def main():
    """get score number, choose random scores, and print results of it"""
    score_no = get_score()

    # choose out random scores as much as input number
    for i in range(score_no):
        random_score = random.randint(0, 101)
        result_message = decide_message(random_score)
        print(f"{random_score} is {result_message}")
    print(END_SCRIPT)


def get_score():
    """get score and validate"""
    score_no = int(input("Enter number of scores: "))
    while score_no < INVALID_SCORE_MINIMUM:
        print(ERROR_SCRIPT)
        score_no = int(input("Enter number of scores: "))
    return score_no


def decide_message(random_score):
    """show appropriate message for random score"""
    if random_score >= EXCELLENT_SCORE:
        result_message = "Excellent"
    elif random_score >= PASSABLE_SCORE:
        result_message = "Passable"
    else:
        result_message = "Bad"
    return result_message


main()
