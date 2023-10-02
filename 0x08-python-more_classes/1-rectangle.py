#!/usr/bin/python3
"""
Define a class `` Rectangle`` with size ``width`` and ``height``
"""


class Rectangle:
    """
    Defines a rectangle with size `` width`` and ``height``
    """

    def __init__(self, width=0, height=0):
        """
        Initialize ``Rectangle``

        Args:
            width: width of ``Rectangle``
            height: height of ``Rectangle``
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns the width of ``Rectangle`` """
        return self.__width

    @width.setter
    def width(self, value):
        """
        gets width of ``Rectangle``

        Arg:
            value (int): value of thd width of ``Rectangle``
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Return the height of ``Rectangle`` """
        return self.__height

    @height.setter
    def height(self, value):
        """
        gets the height of ``Rectangle``

        Arg:
            value (int): value of height of ``Rectangle``
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value