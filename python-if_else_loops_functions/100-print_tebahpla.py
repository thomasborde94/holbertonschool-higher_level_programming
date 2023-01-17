#!/usr/bin/python3
def print_alpha():
    result = ""
    for i in range(122, 96, -1):
        if i % 2 != 0:
            i -= 32
        print("{}".format(chr(i)), end="")
        if i % 2 != 0:
            i += 32

print_alpha()
