#!/usr/bin/python3
"""
Returns lists of available attributes and methods
"""


def lookup(obj):
    """ Return all available attributes and methods in a class"""
    list = dir(obj)
    return list
