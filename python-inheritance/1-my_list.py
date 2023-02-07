#!/usr/bin/python3
"""defines MyList class"""


class MyList(list):
    """implements sorted printing function"""
    def print_sorted(self):
        print(sorted(self))
