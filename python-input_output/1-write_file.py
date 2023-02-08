#!/usr/bin/python3
"""define write_file function"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns\
    number of characters written"""
    with open(filename, "w", encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)
