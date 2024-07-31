#!/usr/bin/python3

"""This script implements the creation of a square using #."""

def print_square(size):
    """This function prints a square.

    Args:
    size: This is the size length of the square which must be an int.

    Raises:
    TypeError: If size is not an integer
    ValueError: If size is less than 0
    TypeError: If size is float and is less than zero
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        print("#" * size)
