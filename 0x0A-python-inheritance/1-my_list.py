#!/usr/bin/python3
"""
Class MyList inherits from list
"""


class MyList(list):
    """ class that inherits from list"""
    def print_sorted(self):
        """ print sorted list"""
        print(sorted(self))
