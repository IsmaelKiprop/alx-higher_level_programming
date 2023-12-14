#!/usr/bin/python3
"""
Module contain a function that returns True if the object is exactly
an instance of the specified class ; otherwise False
"""


def is_same_class(obj, a_class):
    """ A function that returns True if obj is exactly
    an instance of class a_class otherwise false """
    return type(obj) is a_class
