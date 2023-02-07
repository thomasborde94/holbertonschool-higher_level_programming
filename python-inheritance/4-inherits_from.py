#!/usr/bin/python3
"""defines inherits_from function"""


def inherits_from(obj, a_class):
    """ returns if obj is an instance of a class that inherited \
    from the specified class"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
