#!/usr/bin/python3
"""defines save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    json_object = json.dumps(my_obj)
    with open(filename, "w") as myFile:
        myFile.write(json_object)
