#!/usr/bin/python3
""" write a file"""


def write_file(filename="", text=""):
    """function"""

    n = 0
    with open(filename, "w") as my_file:
        nb_char = my_file.write(str(text))
    my_file.close()
    return (nb_char)
