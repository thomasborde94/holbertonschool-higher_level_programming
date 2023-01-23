#!/usr/bin/python3


def no_c(my_string):
    if my_string is None:
        return None
    else:
        newString = ""
        for i in range(0, len(my_string)):
            y = my_string[i]
            if y != "c" and y != "C" and y is not None:
                newString += my_string[i]
        return newString
