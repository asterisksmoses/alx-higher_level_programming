#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) <= 0:
        return None
    else:
        max_py = my_list[0]
        for x in range(len(my_list)):
            if my_list[x] > max_py:
                max_py = my_list[x]
            return max_py
