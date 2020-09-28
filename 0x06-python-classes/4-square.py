#!/usr/bin/python3
"""Create an empty class"""


class Square:
    """This class that defines a square"""
    def __init__(self, size=0):
        """size is private"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """define area"""
        return (self.__size * self.__size)

    @property
    def size(self):
        """define size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
