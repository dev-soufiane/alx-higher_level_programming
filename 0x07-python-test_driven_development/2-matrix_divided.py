#!/usr/bin/python3
"""Matrix division"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    :param matrix: A list of lists containing integers or floats.
    :param div: A non-zero number (integer or float) used for division.

    :raises:
        TypeError: If the matrix is not a list of lists of integers/floats
                   or if each row of the matrix is not of the same size.
        ZeroDivisionError: If div is equal to 0.

    :return: A new matrix with elements rounded to 2 decimal places.
    """
    import decimal

    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if type(matrix) is not list:
        raise TypeError(error_msg)

    row_lengths = []
    row_count = 0

    for row in matrix:
        if type(row) is not list:
            raise TypeError(error_msg)
        row_lengths.append(len(row))

        for element in row:
            if type(element) not in [int, float]:
                raise TypeError(error_msg)

        row_count += 1

    if len(set(row_lengths)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(lambda row:
                          list(map(lambda x: round(x / div, 2), row)), matrix))
    return new_matrix
