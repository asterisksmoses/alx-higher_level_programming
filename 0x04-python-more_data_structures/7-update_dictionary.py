#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if not isinstance(key, str):
        raise ValueError("Key argument should always be a string")
    a_dictionary[key] = value
    return a_dictionary
