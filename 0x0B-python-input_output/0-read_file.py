#!/usr/bin/python3
"""create"""


def read_file(filename=""):
    """read file function"""

    with open(filename, "r") as my_file:
        print(my_file.read(), end="")
    my_file.close()
