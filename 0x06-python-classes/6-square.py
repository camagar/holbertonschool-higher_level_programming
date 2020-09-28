#!/usr/bin/python3
"""Create an empty class"""


class Square:
    """This class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """size is private"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2 or\
           type(position[0]) != int or type(position[1]) != int or\
           position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """print the square"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                for i in range(self.__position[0]):
                    print("{}".format(" "), end="")
                for i in range(self.__size):
                    print("{}".format("#"), end="")
                print()

    @property
    def position(self):
        """def position"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if type(value) is not tuple or len(value) !=\
           2 or type(value[0]) != int or\
           type(value[0]) != int or value[0] < 0 or value[1] < 1:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
