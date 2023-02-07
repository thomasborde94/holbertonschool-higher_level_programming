#!/usr/bin/python3
"""defines is_same_class func"""


def is_same_class(obj, a_class):
    """returns true if obj is instance of class"""
    if type(obj) is a_class:
        return True
    else:
        return False
