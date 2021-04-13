#!/usr/bin/python3
""" find peak"""


def find_peak(list_of_integers):
    """Find peak"""
    if len(list_of_integers) == 0:
        return None
    list_of_integers.sort(reverse=True)
    return list_of_integers[0]
