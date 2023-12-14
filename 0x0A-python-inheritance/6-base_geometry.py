#!/usr/bin/python3
""" Module with class that raise exception when called"""


class BaseGeometry:
    """A class that raises an Exception with the
    message area() is not implemented"""
    def area(self):
        raise Exception("area() is not implemented")
