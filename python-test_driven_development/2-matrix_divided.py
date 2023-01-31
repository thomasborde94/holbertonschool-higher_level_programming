#!/usr/bin/python3
"""Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides every element of a matrix by div
    Args:
        matrix (list of ints or float): first parameter
        div (int or float): second parameter
    Return: a new matrix
    """
    if not isinstance(matrix, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(i/div, 2) for i in row] for row in (matrix)]
