#!/usr/bin/python3
def uppercase(str):
    result = ""
    for character in str:
        if 97 <= ord(character) <= 122:
            ord(character) -= 32
        result += character
    print("{}".format(result))

