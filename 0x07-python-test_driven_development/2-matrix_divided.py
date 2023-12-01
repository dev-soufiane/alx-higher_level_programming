#!/usr/bin/python3
"""
This module introduces a function for dividing matrices.
"""


def matrix_divided(matrix, div):
    """
    Perform matrix division by a specified number.

    Args:
        matrix: A list of lists (matrix) where members can be int or floats.
        div: Number to be used for the division (can be a float or an integer).

    Raises:
        TypeError: If the matrix contains non-numeric elements.
        TypeError: If the matrix has rows of varying sizes.
        TypeError: If div is not an integer or float.
        ZeroDivisionError: If div is 0.

    Returns:
        A new matrix representing the result of the divisions.
        """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
