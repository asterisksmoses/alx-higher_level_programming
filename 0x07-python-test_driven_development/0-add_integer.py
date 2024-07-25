#!/usr/bin/python3

def add_integer(a, b=98):
    """This function computes the sum of 2 integers.

    Parameters:
    a: int or float - The first number to be added.
    b: int or float - The second number to be added.

    Raises:
    TypeError: If either a or b is not an integer or a float.

    Returns:
    This function returns the computed sum of the two integers.

    Examples:
    >>> add_integer(1, 2)
    3

    >>> add_integer(1.5, 2.5)
    4

    >>> add_integer(1)
    99
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer
    >>> add_integer(2, "b")
    Traceback (most recent call last):
        ...
    TypeError: b must be an integer
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a+b
