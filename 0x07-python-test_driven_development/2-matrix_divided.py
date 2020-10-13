#!/usr/bin/python3
"""def. of the function"""


def matrix_divided(matrix, div):
    """matrix divided function"""
    if not matrix or type(matrix) != list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")
    if isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if type(matrix[i][j]) is not int and type(matrix[i][j]) is not\
                float:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats ")
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix2 = list(map(lambda i: list(map(lambda j: j / div, i)), matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix2[i][j] = round(matrix2[i][j], 2)
    return matrix2
