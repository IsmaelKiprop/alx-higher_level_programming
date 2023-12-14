#!/usr/bin/python3
""" A locked class"""


class LockedClass:
    """ Lock class atribute"""
    __slots__ = 'first_name'

    def __init__(self, first_name=None):
        self.first_name = first_name
