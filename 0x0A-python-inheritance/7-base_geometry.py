#!/usr/bin/python3
""" Module with class that validate integer"""


class BaseGeometry:
    """A class that validate integer"""

    def integer_validator(self, name, value):
        """Validates name/value argument
        Arguments:
            name: name associated with value
            value: value (must be integer > 0)
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        return True

    def area(self):
        """ Calc area of a shape"""
        raise Exception("area() is not implemented")
