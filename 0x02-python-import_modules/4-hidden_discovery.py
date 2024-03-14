#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    all_fr = dir()
    for x in range(0, len(all_fr)):
        if all_fr[x][:2] != "__":
            print("{:s}".format(all_fr[x]))
