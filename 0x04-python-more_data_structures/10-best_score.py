#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Function that returns a key with the biggest integer value.
    """
    best_key = None
    best_score = float('-inf')

    if a_dictionary is not None:
        for key, val in a_dictionary.items():
            if val > best_score:
                best_score = val
                best_key = key

    return best_key
