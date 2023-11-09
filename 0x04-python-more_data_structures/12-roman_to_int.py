#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Function that converts a Roman numeral to an integer.
    """

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    prev_val = 0

    for c in reversed(roman_string):
        val = roman_dict[c]
        if val >= prev_val:
            result += val
        else:
            result -= val
        prev_val = val

    return result
