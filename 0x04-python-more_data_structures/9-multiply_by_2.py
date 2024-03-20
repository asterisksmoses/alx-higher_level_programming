#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    multiples_new = {}
    for key, value in a_dictionary.items():
        multiples_new[key] = value * 2
    return multiples_new
