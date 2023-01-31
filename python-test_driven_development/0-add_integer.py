#!/usr/bin/python3
"""Defines an integer adition function
"""


def add_integer(a, b=98):
    """
    Adds a and b and returns sum
    Args:
        a (int): first parameter
        b (int): second parameter
    Return:
        sum of a + b
    """
    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
