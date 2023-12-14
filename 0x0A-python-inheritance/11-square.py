#!/usr/bin/python3
""" Class Square that inherits from Rectangle. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle. """
    def __init__(self, size):
        """ Instantiation with size. """
        self.__size = size
        self.integer_validator('size', size)
        super().__init__(size, size)

    def __str__(self):
        """ Public method for printed string representation. """
        return ("[Square] {}/{}".format(self.__size, self.__size))
