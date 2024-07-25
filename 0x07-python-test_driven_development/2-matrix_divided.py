#!/usr/bin/python3

def matrix_divided(matrix, div):
    """This function divides all the elements of a matrix.

    Paramaters:
    matrix: List of int or float - The values to be divided.
    div: int or float - The dividing component

    Raises:
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    TypeError: Each row of the matrix must have the same size
    TypeError: div must be a number
    ZeroDivisionError: division by zero

    Returns:
    A new matrix

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> div = 2
        >>> matrix_divided(matrix, div)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]

        >>> matrix = [[1.5, 2.5, 3.5], [4.5, 5.5, 6.5]]
        >>> div = 2.5
        >>> matrix_divided(matrix, div)
        [[0.6, 1.0, 1.4], [1.8, 2.2, 2.6]]

        >>> matrix = [[1, 2, 3]]
        >>> div = 1
        >>> matrix_divided(matrix, div)
        [[1.0, 2.0, 3.0]]

        """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_lens = [len(row) for row in matrix]
    if len(set(row_lens)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    n_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return n_matrix
