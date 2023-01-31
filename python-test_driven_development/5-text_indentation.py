#!/usr/bin/python3
"""prints a text"""


def text_indentation(text):
    """ prints a text with 2 new lines after\
specific characters
    Args:
        text (string): first parameter
    Return:
        nothing
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    for i in text:
        if i != "." and i != "," and i != "?" and i != ":":
            print("{}".format(i), end="")
        else:
            print()
            print()
