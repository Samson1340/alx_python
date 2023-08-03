#!/usr/bin/python3
"""
Module consists of a class Rectangle that
inherits from BaseGeometry.
"""
BaseGeometry = __import__('5-base_geometry.py').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry."""
    def __init__(self, width, height):
        """Instanciation with width and height.
        Args:
            width: width of rectangle.
            height: Height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
