#!/usr/bin/python3
""" Writes object to text file, using a JSON representation """


def save_to_json_file(my_obj, filename):
    """ Write object to text file with JSON

    Arguments:
        my_obj: object to write
        filename: file to write to
    """

    import json

    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
