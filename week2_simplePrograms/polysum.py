# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:12:10 2020

@author: Effy‘s PC
6.00.1x, week 2 
Complete Programming Experience: polysum
"""
"""
Grader
10.0/10.0 points (ungraded)
A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 0.25∗n∗s2tan(π/n)
The perimeter of a polygon is: length of the boundary of the polygon
Write a function called polysum that takes 2 arguments, n and s. This function should sum the area and square of the perimeter of the regular polygon. The function returns the sum, rounded to 4 decimal places.
This is an optional exercise, but great for extra practice!
"""
import math
def polysum(n,s):
    a = math.tan(math.pi/n)
    area = 0.25*n*s**2/a
    parimeter = n*s
    return round(area + parimeter**2, 4)
#Correct
