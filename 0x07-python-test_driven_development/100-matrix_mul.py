#!/usr/bin/python3
"""Matrix Multiplication Function"""


def matrix_mul(m_a, m_b):
    """
     Args:
         Multiplies two matrices using the NumPy module.
         :param m_a: List of lists containing integers or floats.
         :param m_b: List of lists containing integers or floats.

    Raises:
        TypeError:
            If m_a and m_b are not lists of lists.
            If any element in the matrices is not an integer or a float.
            If matrices are not rectangle.

        ValueError:
            If m_a or m_b is empty (it means: = [] or = [[]]).
            If matrices cannot be multiplied.
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")

    # variables to verify if both m_a and m_b can be multiplied
    num_columns_a = 0
    num_rows_b = 0

    # Check requirements for matrix m_a
    if m_a == []:
        raise ValueError("m_a can't be empty")
    for row_a in m_a:
        if type(row_a) != list:
            raise TypeError("m_a must be a list of lists")
        len_a = len(m_a[0])
        if row_a == []:
            raise ValueError("m_a can't be empty")
        if len_a != len(row_a):
            raise TypeError("each row of m_a must be of the same size")
        num_columns_a = len(row_a)
        for column_a in row_a:
            if type(column_a) != int and type(column_a) != float:
                raise TypeError("m_a should contain only integers or floats")

    # Check requirements for matrix m_b
    if m_b == []:
        raise ValueError("m_b can't be empty")
    for row_b in m_b:
        if type(row_b) != list:
            raise TypeError("m_b must be a list of lists")
        len_b = len(m_b[0])
        if row_b == []:
            raise ValueError("m_b can't be empty")
        if len_b != len(row_b):
            raise TypeError("each row of m_b must be of the same size")
        num_rows_b += 1
        for column_b in row_b:
            if type(column_b) != int and type(column_b) != float:
                raise TypeError("m_b should contain only integers or floats")

    # Check if the multiplication is possible
    if num_columns_a != num_rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    multiplication_result = []

    for row_1 in m_a:
        x = 0
        result_row = []
        while x < len(m_b[0]):
            result = 0
            k = 0
            for column_1 in row_1:
                result += column_1 * m_b[k][x]
                k += 1
            result_row.append(result)
            x += 1
        multiplication_result.append(result_row)

    return multiplication_result
