#!/usr/bin/python3
"""
This module contains a class that defines a Square.
"""


class Square:
    """A class that defines a square.
    """
    def __init__(self, size=0):
        """Initializes the class and all it's instances.
            Args:
                size (int): Size of the Square.
        """
        self.__size = size

    @property
    def size(self):
        """A getter that gets the size of the Square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Checks if the size value got earlier is valid.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square with the character #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end='')
                print()