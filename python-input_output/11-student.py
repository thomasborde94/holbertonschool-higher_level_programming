#!/usr/bin/python3
"""defines class Student"""


class Student():
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            dict = {}
            for key, value in self.__dict__.items():
                for el in attrs:
                    if key == el:
                        dict[key] = value
            return dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
