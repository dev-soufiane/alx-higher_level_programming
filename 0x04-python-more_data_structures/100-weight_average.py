#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    Function that returns the weighted average of all integers tuple.
    """

    if len(my_list) == 0:
        return 0
    
    sum_score = 0
    sum_weight = 0

    for score, weight in my_list:
        sum_score += score * weight
        sum_weight += weight

    return (sum_score / sum_weight)
