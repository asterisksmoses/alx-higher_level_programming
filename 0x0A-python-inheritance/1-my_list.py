#!/usr/bin/python3
"""A module that supports basic list inheritance."""


class MyList(List):
    """A derived (MyList) inheriting from a Base class (List)"""
    def print_sorted(self):
        """A method for printing out a sorted list."""
        print(sorted(self))
