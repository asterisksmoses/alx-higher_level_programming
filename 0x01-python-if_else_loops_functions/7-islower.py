#!/usr/bin/python3
def islower(c):
    if ord('a') <= ord(c) <= ord('z'):
        return f"{c} is lower"
    elif ord('A') <= ord(c) <= ord('Z'):
        return f"{c} is upper"
    else:
        return f"{c} is not alphabetic"
