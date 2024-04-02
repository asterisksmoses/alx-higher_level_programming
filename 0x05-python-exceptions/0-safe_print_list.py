#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements_print = 0

    for y in range(x):
        try:
            print(my_list[y], end='')
            elements_print += 1
        except IndexError:
            break
    print()
    return elements_print
