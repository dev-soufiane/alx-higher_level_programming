#!/usr/bin/python3
"""
    This module defines a function def pascal_triangle(n):
    that returns a list of lists of integers representing
    the pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the pascal’s triangle of n.
    """
    if (n <= 0):
        return ([])
    elif (n == 1):
        return ([[1]])
    elif (n == 2):
        return ([[1], [1, 1]])

    pasc = [[1], [1, 1]]

    for i in range(1, n - 1):
        myList = []
        myList.append(1)
        for j in range(1, len(pasc)):
            myList.append(pasc[i][j - 1] + pasc[i][j])
        myList.append(1)
        pasc.append(myList)

    return (pasc)
