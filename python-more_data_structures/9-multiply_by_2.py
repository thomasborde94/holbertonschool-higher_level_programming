#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    newDic = a_dictionary.copy()
    newDic.update((x, y * 2) for x, y in newDic.items())
    return newDic
