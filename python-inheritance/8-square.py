#!/usr/bin/python3
"""
Module consists of a class Square that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class square that inherits from Rectangle."""
    def __init__(self, size):
        """Instantiation of class."""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Method that returns the area"""
        return super().area()