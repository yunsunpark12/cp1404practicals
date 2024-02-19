import random

ERROR_SCRIPT = "Invalid score"
SCORE_SCRIPT_90 = "Excellent"
SCORE_SCRIPT_50 = "Passable"
SCORE_SCRIPT_BAD = "bad"


def main():
    score = float(input("Enter score: "))
    result_message = decide_message(score)
    print(result_message)

    # print random score and result of it
    random_score = random.randint(0,100)
    print("Random score: ", random_score)
    result_random_message = decide_message(random_score)
    print("Result for random score: ", result_random_message)


def decide_message(score):
    if score < 0 or score > 100:
        result_message = ERROR_SCRIPT
    elif score >= 90:
        result_message = SCORE_SCRIPT_90
    elif score >= 50:
        result_message = SCORE_SCRIPT_50
    else:
        result_message = SCORE_SCRIPT_BAD
    return result_message


main()