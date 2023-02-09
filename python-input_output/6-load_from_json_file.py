#!/usr/bin/python3
"""defines load_from_json_file function"""
import json


def load_from_json_file(filename):
    """creates an object from a json file"""
    with open(filename, "r") as myFile:
        return json.load(myFile)
