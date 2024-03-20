#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_list = []

    for element in my_list:
        if element == search:
            nw_list.append(replace)
        else:
            nw_list.append(element)
        return nw_list
