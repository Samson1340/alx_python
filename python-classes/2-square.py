#!/usr/bin/python3
"""
This module contains a class that defines a Square.
"""


class Square:
    """ A class that defines a Square.
    """
    def __init__(self, size=0):
        """ Initializes the class and its instances.
            Args:
                size (int): Size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ Function that returns the area of the square.
        """
        return self.__size * self.__size