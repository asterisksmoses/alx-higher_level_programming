#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum_int = 0
    for x in range(1, len(argv)):
        sum_int += int(argv[x])
    print("{}".format(sum_int))
