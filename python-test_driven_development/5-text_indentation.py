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
    a = 0
    while a < len(text):
        if text[a] in [':', '.', '?']:
            print(text[a])
            print()
            a += 1
        else:
            print(text[a], end='')
            a += 1
