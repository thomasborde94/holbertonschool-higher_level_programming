#!/usr/bin/python3
"""defines append_write function"""


def append_write(filename="", text=""):
    """appends a text to a file"""
    with open(filename, "a", encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)
