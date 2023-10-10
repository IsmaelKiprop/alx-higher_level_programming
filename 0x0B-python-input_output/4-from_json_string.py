#!/usr/bin/python3
""" Deserialize to JSON """


def from_json_string(my_str):
    """ Deserialize json str to obj"""

    import json

    return json.loads(my_str)
