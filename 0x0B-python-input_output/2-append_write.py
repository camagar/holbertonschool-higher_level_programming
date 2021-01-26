#!/usr/bin/python3
""" write a file"""


def append_write(filename="", text=""):
    """append write"""

    with open(filename, "a") as my_file:
        New = my_file.write(text)
    return (New)