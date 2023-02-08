#!/usr/bin/python3
"""defines BaseGeometry and Rectangle classes"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Rectangle(BaseGeometry):
    """defines Rectangle which inherits from basegeo"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        area = self.__width * self.__height
        return area

    def __str__(self):
        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string

class Square(Rectangle):
    """defines Square which inherits from rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
