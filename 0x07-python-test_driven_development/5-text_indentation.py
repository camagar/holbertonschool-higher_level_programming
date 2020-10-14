#!/usr/bin/python3
"""Def a function"""


def text_indentation(text):
    """Def"""
    if type(text) is not str:
        raise TypeError('text must be a string')
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i])
            print()
        else:
            if text[i] == " " and (text[i - 1] in [".", "?", ":", " "]):
                continue
            print(text[i], end="")
