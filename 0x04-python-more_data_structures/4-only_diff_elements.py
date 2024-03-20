#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_els = set_1.difference(set_2)
    diff_els_x = set_2.difference(set_1)
    final_els = diff_els.union(diff_els_x)
    return final_els
