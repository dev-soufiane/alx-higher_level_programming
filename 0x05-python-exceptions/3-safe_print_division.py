#!/usr/bin/python3
def safe_print_division(a, b):
    """Function that divides 2 integers and prints the result."""
    res = None
    try:
        res = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {:.1f}".format(res))
    return res
