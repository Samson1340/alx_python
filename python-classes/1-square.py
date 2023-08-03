#!/usr/bin/python3
"""
This module is composed by a class that defines a Square.
"""


class Square:
    """This is a class that defines a Square.
    """
    def __init__(self, size=0):
        """ Initialization of the instance attributes
            Args:
            size (int): The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size