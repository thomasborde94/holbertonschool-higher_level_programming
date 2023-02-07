#!/usr/bin/python3
"""defines is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """ returns true if obj is instance of a_class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
