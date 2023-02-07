#!/usr/bin/python3
""" defines lookup"""


def lookup(obj):
    """returns list of variables and methods of an object"""
    list_a = dir(obj)
    return list_a
