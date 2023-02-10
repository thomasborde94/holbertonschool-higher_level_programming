#!/usr/bin/python3
"""Triangle Pascal"""


def pascal_triangle(n):
    """Triangle pascal"""

    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            myList = [1]
            for j in range(i - 1):
                myList.append(triangle[i - 1][j] + triangle[i - 1][j + 1])
            myList.append(1)
            triangle.append(myList)
    return triangle
