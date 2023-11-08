#!/usr/bin/python3

def uniq_add(my_list=[]):
    """Function that adds all unique integers
    in a list (only once for each integer)."""

    unique_set = set(my_list)
    new_list = list(unique_set)
    sum = 0

    for num in new_list:
        sum += num

    return sum
