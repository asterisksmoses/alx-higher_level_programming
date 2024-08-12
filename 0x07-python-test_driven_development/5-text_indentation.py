#!/usr/bin/python3

"""This script is of a function that prints 2 new lines after any
of these characters is enountered ., ?, :."""

def text_indentation(text):
    """This  function prints 2 new lines after enountering any of
    these ., ?, :

    Args:
    text: The text to be printed which must be a string.

    Raises:
    TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    x = 0
    while x < len(text):
        print(text[x], end='')
        if text[x] in characters:
            print('\n')
            while x + 1 < len(text) and text[x + 1] == ' ':
                x += 1

        x += 1
