#!/usr/bin/python3
"""defines to_json_string func"""
import json


def to_json_string(my_obj):
    """return the json representation of an object"""
    return json.dumps(my_obj)
