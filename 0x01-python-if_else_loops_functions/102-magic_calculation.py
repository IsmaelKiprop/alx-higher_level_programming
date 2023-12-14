#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(x, y, z):
    """Match bytecode provided by Holberton School."""
    if x < y:
        return (z)
    if z > y:
        return (x + y)
    return (x*y - z)
