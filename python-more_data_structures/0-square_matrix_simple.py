#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    newMatrix = [list(map(lambda x: x * x, y)) for y in matrix]
    return newMatrix
