#!/usr/bin/python3
"""Module for the lookup method."""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    A function that takes an object as an argument amd returns the a
    list of the attributes and methods that are available on the object

    Parameters:
    obj : The object for which to list variable methods and attributes

    Returns: A list of strings representing the names of attributes
    and methods available on the object.

    """
    return dir(obj)
