# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:26:07 2020

@author: Effy‘s PC
6.00.1x, week 3
Finger Exercise
"""
"""
Exercise: odd tuples
 Bookmark this page
Exercise: odd tuples
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 5 minutes

Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, where every other element of the input tuple is copied, starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
"""
def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    result = ()
    for i in range(len(aTup)):
       if i % 2 == 0:
           result = result + (aTup[i],) 
    return result
#Correct
    
"""
Exercise: apply to each 1
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 2 minutes

Here is the code for a function applyToEach:

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
Assume that

testList = [1, -4, 8, -9]
For each of the following questions (which you may assume is evaluated independently of the previous questions, so that testList has the value indicated above), provide an expression using applyToEach, so that after evaluation testList has the indicated value. You may need to write a simple procedure in each question to help with this process.

Example Question:

>>> print(testList)
[5, -20, 40, -45]
Solution to Example Question
  >>> print(testList)
  [1, 4, 8, 9]
"""
def afunc(a):
    return abs(a)
    
applyToEach(testList, afunc)
#Correct

"""
Exercise: how many
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 6 minutes

Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
We want to write some simple procedures that work on dictionaries to return information.

First, write a procedure, called how_many, which returns the sum of the number of values associated with a dictionary. For example:

>>> print(how_many(animals))
6
"""
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    values =  aDict.values()
    result = 0
    for lst in values:
        count = 0
        for i in lst:
            count += 1
        result += count
    return result
#Correct
    
"""
Exercise: biggest
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 7 minutes

Consider the following sequence of expressions:

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
We want to write some simple procedures that work on dictionaries to return information.

This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

Example usage:

>>> biggest(animals)
'd'
If there are no values in the dictionary, biggest should return None.
"""
def biggest(aDict):
    if aDict.values == []:
        return None
    lenths = {}
    for key in aDict:
        lenths[key] = len(aDict[key])
    
    for key2 in lenths:
        if lenths[key2] == max(lenths.values()):
            return str(key2)
#Correct
            

    