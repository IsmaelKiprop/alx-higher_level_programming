#!/usr/bin/python3

""" Module contains func that read and print out text file """


def read_file(filename=""):
    """ Read  and print out text file to stdout"""
    with open(filename) as f:
        print(f.read(), end="")
