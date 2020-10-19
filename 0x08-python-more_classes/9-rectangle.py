#!/usr/bin/python3
"""create a class"""


class Rectangle(object):
    """define the rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                    print_rectangule += str(self.print_symbol)
                if i != (self.__height - 1):
                    print_rectangule += "\n"
        return print_rectangule

    def __repr__(self):
        """representation"""
        reptangle = 'Rectangle(' + str(self.__width) + ', ' +\
            str(self.__height) + ')'
        return (reptangle)

    def __del__(self):
        """del instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """static method"""
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """class method"""
        new_square = cls(size, size)
        return new_square
