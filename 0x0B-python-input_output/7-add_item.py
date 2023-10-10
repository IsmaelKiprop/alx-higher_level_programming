#!/usr/bin/python3
"""
Adds all arguments to a Python list, and then save
them to a JSON file
"""
import json
from sys import argv
from os.path import exists

if __name__ == "__main__":
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file

    if not exists("add_item.json"):
        with open("add_item.json", mode="w", encoding="utf-8") as f:
            f.write('[]')

    obj = load("add_item.json")
    for arg in argv[1:]:
        obj.append(arg)

    save(obj, "add_item.json")
