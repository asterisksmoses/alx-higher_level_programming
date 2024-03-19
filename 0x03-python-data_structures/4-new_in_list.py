#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    temp_py = my_list[:]
    if idx < 0:
        return temp_py
    if idx > len(my_list) - 1:
        return temp_py
    temp_py[idx] = element
    return temp_py
