#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    y = len(argv) - 1
    if y < 1:
        print("{} arguments.".format(y))
    elif y == 1:
        print("{} argument:".format(y))
    else:
        print("{} arguments:".format(y))

    for y in range(y):
        print("{}: {}".format())
