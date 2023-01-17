#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    string = ""
    for char in str:
        if i == n:
            i++
            continue
        else:
            string += str(char)
        i++
    print("{}".format(string))
