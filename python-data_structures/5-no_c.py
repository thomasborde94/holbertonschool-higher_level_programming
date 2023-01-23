#!/usr/bin/python3


def no_c(my_string):
    if my_string is None:
        return None
    else:
        newString = ""
        for i in range(0, len(my_string)):
            if my_string[i] != "c" and my_string[i] != "C" and my_string[i] != None:
                newString += my_string[i]
        return newString
