#!/usr/bin/env python3
def no_c(my_string):
    Nstr = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            Nstr += char
    return (Nstr)
