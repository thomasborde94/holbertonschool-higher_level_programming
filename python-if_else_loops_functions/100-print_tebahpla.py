#!/usr/bin/python3
def print_alpha():
    result = ""
    for i in range(123, 97):
        if i % 2 == 0:
            i = chr(ord(i) - 32)
        result += i
    print("{}".format(result), end="")
