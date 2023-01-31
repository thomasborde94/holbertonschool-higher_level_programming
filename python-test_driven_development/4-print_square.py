#!/usr/bin/python3
"""prints a square with #
"""


def print_square(size):
    """
    prints a square of size size with #
    Args:
        size (int): first parameter
    Return: nothing
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
