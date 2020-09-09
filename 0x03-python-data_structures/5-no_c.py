#!/usr/bin/python3
def no_c(my_string):
    Nstr = my_string
    return(Nstr.translate({ord('c'): None, ord('C'): None}))
