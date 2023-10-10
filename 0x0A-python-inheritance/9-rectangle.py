#!/usr/bin/python3
""" Class Rectangle that ingerits from BaseGeometry. """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle that inherits from BaseGeometry. """
    def __init__(self, width, height):
        """ Instantiation of width and height. """
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)

    def area(self):
        """Implementing Public method area"""
        return self.__width * self.__height

    def __str__(self):
        """ Public method for printed string representation. """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
