#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    string = ""
    for char in str:
        if i == n:
            i += 1
            continue
        else:
            string += char
        i += 1
    print("{}".format(string))
