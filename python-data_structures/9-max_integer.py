#!/usr/bin/python3


def max_integer(my_list=[]):
    x = 0
    if len(my_list) == 0:
        return None
    for i in range(1, len(my_list)):
        if my_list[i] > my_list[i - 1] and my_list[i] > x:
            x = my_list[i]
    return x
