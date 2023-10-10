#!/usr/bin/python3
""" Serialize to JSON """


def to_json_string(my_obj):
    """ Serialize obj to json str"""

    import json

    return json.dumps(my_obj)
