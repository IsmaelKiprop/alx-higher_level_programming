#!/usr/bin/python3
"""
Module contain a function that returns True if the object
is an instance of, or if
the object is an instance of a class that inherited from,
the specified class ; otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """ A function that returns True if obj is an instance of
      class a_class or subclass, otherwise false"""
    return isinstance(obj, a_class)
