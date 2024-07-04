#!/usr/bin/python3

def find_peak(list_of_integers):
    """This function finds the peak in a list of integers."""
    if list_of_integers == []:
        return None

    x = len(list_of_integers)
    if x == 0:
        return (None)
    elif x == 1:
        return (list_of_integers[0])
    elif x == 2:
        return max(list_of_integers)

    mid = int(x/2)
    peak = list_of_integers[mid]
    my_list = list_of_integers
    if peak > my_list[mid - 1] and peak > my_list[mid + 1]:
        return peak
    elif peak < my_list[mid - 1]:
        return find_peak(my_list[mid:])
    else:
        return find_peak(my_list[mid + 1:])
