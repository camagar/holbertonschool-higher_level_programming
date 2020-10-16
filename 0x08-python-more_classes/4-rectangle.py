#!/usr/bin/python3
"""create a class"""


class Rectangle(object):
    """define the rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width"""
        return self.__width

    @property
    def height(self):
        """height"""
        return self.__height

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """area"""
        a = self.__width * self.__height
        return a

    def perimeter(self):
        """Perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            p = (self.__width * 2) + (self.__height * 2)
            return p

    def __str__(self):
        """string method"""
        print_rectangule = ""
        if self.__width == 0 or self.__height == 0:
            return print_rectangule
        else:
            for i in range(0, self.__height):
                for j in range(0, self.__width):
                    print_rectangule += "#"
                if i != (self.__height - 1):
                    print_rectangule += "\n"
        return print_rectangule

    def __repr__(self):
        """representation"""
        reptangle = 'Rectangle(' + str(self.__width) + ', ' +\
            str(self.__height) + ')'
        return (reptangle)
