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
    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:,":
            if text[c] in ".?:,":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
