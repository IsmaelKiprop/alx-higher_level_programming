#!/usr/bin/python3
""" Module with a class that defines student"""


class Student:
    """Class Student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            filterDict = {}
            for key in attrs:
                if type(key) is str and key in self.__dict__:
                    filterDict.update({key: self.__dict__[key]})
            return filterDict
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of a Student instance"""
        for key, value in json.items():
            self.__dict__[key] = value
