#!/usr/bin/python3
"""A square module."""


class Square:
    """A class to represent a Square."""
    def __init__(self, size=0):
        """Constructor


        Args:
        size (int): The length of one side of the square
        """
        self.__size = int(size)


    def get_size(self):
        """A Getter way to retrieve the size of the square."""
        return self.__size


    def set_size(self, value):
        """A size setter method the set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    size = property(get_size, set_size)

    def area(self):
        """Finds the area of the square"""
        return self.__size ** 2
