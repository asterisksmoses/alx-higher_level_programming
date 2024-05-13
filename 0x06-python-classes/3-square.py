#!/usr/bin/python3
"""A square module."""


class Square:
    """A class to represent a Square."""
    def __init__(self, size=0):
        """Constructor


        Args:
        size (int): The length of one side of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Finds the area of the square"""
        return self.__size ** 2
