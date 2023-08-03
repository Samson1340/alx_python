#!/usr/bin/python3
"""
This module contains a class that defines a Square.
"""


class Square:
    """ This is a class that defines a square.
    """
    def __init__(self, size=0):
        """ Initializes the class and all its instances.
            Args:
                size (int): Size of the class.
        """
        self.__size = size

    @property
    def size(self):
        """Getter for the size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Check if the value given are valid and sets the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the area of the square
        """
        return (self.__size * self.__size)