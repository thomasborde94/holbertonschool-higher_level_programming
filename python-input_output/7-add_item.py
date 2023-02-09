#!/usr/bin/python3
"""defines a script that adds all arguments to a Python list,\
 and then save them to a file"""
import sys
import json


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file')\
        .load_from_json_file
    args = sys.argv
    try:
        my_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        my_list = []
    my_list.extend(args[1:])
    save_to_json_file(my_list, "add_item.json")
