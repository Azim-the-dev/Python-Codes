# Write a menu-driven program, using user-defined functions to find the area of rectangle,  square, circle and triangle by accepting suitable input parameters from user. 

import math

def rec_area(length, width):
    return length * width

def squ_area(side):
    return side * side

def cir_area(radius):
    return math.pi * radius**2

# # #