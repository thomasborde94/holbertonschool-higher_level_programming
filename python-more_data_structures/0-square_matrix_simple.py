#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    newMatrix = matrix.copy()
    for i in range(len(newMatrix)):
        for j in range(len(newMatrix[i])):
            newMatrix[i][j] = (newMatrix[i][j]) ** 2
    return newMatrix
