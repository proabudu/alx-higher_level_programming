#!/usr/bin/python3
""""
Imports the 0-rectangle module and its Rectangle class for use.
Creates a new instance of the Rectangle class named my_rectangle.
"""

Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)
