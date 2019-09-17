def average(score_list):
    total = 0

    for value in score_list:
        total = total + value

    return total / len(score_list)
