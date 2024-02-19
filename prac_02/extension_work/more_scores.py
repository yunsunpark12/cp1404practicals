import random

ERROR_SCRIPT = "Invalid input"
SCORE_SCRIPT_90 = "Excellent"
SCORE_SCRIPT_50 = "Passable"
SCORE_SCRIPT_BAD = "Bad"
END_SCRIPT = "Finished"

def main():
    score_no = int(input("Enter number of scores: "))
    while score_no < 0:         # error check
        print(ERROR_SCRIPT)
        score_no = int(input("Enter number of scores: "))

    # choose out random scores as much as input number
    for i in range(score_no):
        random_score = random.randint(0, 101)
        result_message = decide_message(random_score)
        print(f"{random_score} is {result_message}")
    print(END_SCRIPT)

# show appropriate message for random score
def decide_message(random_score):
    if random_score >= 90:
        result_message = SCORE_SCRIPT_90
    elif random_score >= 50:
        result_message = SCORE_SCRIPT_50
    else:
        result_message = SCORE_SCRIPT_BAD
    return result_message


main()
