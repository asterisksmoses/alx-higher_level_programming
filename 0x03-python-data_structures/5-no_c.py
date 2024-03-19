#!/usr/bin/python3
def no_c(my_string):
    if my_string[:]:
        string_a = my_string.translate({ord("c"): None})
        string_b = my_string.translate({ord("C"): None})
        return string_b
    return my_string
