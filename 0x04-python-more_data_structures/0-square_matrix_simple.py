#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return None
    nMatrix = list(map(lambda i: list(map(lambda j: j * j, i)), matrix))
    return nMatrix
