#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    ints_printed = 0
    for y in range(x):
        try:
            print("{:d}".format(my_list[y]), end='')
            ints_printed += 1
        except (ValueError, TypeError):
            pass
    print()
    return ints_printed
