# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:30:12 2020

@author: Effy‘s PC
6.00.1x, week 4 Good Programming Practices
Finger Exercises
"""
"""
Exercise: integer division
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 4 minutes

Consider the following function definition:

def integerDivision(x, a):
    
    #x: a non-negative integer argument
    #a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    
    while x >= a:
        count += 1
        x = x - a
    return count
When we call

print(integerDivision(5, 3))
we get the following error message:

File "temp.py", line 9, in integerDivision
    count += 1
UnboundLocalError: local variable 'count' referenced before assignment
Your task is to modify the code for integerDivision so that this error does not occur.
"""
def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count
#Correct
    
"""
Exercise: simple divide
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 4 minutes

Suppose we rewrite the FancyDivide function to use a helper function.

def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
   return item / denom
    

This code raises a ZeroDivisionError exception for the following call: fancy_divide([0, 2, 4], 0)

Your task is to change the definition of simple_divide so that the call does not raise an exception. When dividing by 0, fancy_divide should return a list with all 0 elements. Any other error cases should still raise exceptions. You should only handle the ZeroDivisionError.
"""
def simple_divide(item, denom):
    try:  
        return item / denom   
    except ZeroDivisionError:
        return 0 
#Correct