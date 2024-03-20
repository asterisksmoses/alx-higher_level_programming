#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score_ky = None
    max_score = float('-inf')
    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            max_score_ky = key

    return max_score_ky
