#!/usr/bin/python3
"""defines read_file function"""


def read_file(filename=""):
    """reads a text file and prints it"""
    with open(filename, "r", encoding="utf-8") as myFile:
        print(myFile.read(), end="")
