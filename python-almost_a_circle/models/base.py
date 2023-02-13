#!/usr/bin/python3
"""Define Base class"""
import json


class Base:
    """Defines Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string repr of dict"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the json string repr of list_obj to a file"""
        myFile = cls.__name__ + ".json"
        with open(myFile, "w") as buff:
            if list_objs is None:
                buff.write("[]")
            else:
                toDictionary = [lists.to_dictionary() for lists in list_objs]
                buff.write(Base.to_json_string(toDictionary))
