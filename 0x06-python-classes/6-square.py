#!/usr/bin/python3
"""A square module."""


class Square:
    """A class to represent a Square."""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor
        Args:
        size (int): The length of one side of the square
        """
        self.size = int(size)
        self.position = position

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

    def get_position(self):
        """A getter method to retrieve the position of the sqaure."""
        return self.__position

    def set_position(self, value):
        """A setter for the position of the square."""
        if isinstance(value, tuple) and len(value) == 2 and all(isinstance(i, int) 
                for i in value) and all(i >= 0 for i in value):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

        position = property(get_position, set_position)

    def area(self):
        """Finds the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #."""
        if self.__size == 0:
            print()
            return
        for _ in range(self.position[1]):
            print()

        for _ in range(self.size):
            print(" " * self.position[0] +  "#" * self.size)
