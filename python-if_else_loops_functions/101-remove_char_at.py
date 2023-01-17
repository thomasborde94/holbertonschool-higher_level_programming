#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    string = ""
    if n < 0:
        return str
    for char in str:
        if i == n:
            i += 1
            continue
        else:
            string += char
        i += 1
    print("{}".format(string))
