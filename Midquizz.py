# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:07:35 2020

@author: Effy‘s PC
mit 6.00.1 midquizz
"""
#Problem 3
#10/10 points (graded)
#Implement a function called closest_power that meets the specifications below.
#
#def closest_power(base, num):
#    '''
#    base: base of the exponential, integer > 1
#    num: number you want to be closest to, integer > 0
#    Find the integer exponent such that base**exponent is closest to num.
#    Note that the base**exponent may be either greater or smaller than num.
#    In case of a tie, return the smaller value.
#    Returns the exponent.
#    '''
#    # Your code here
#For example,
#
#closest_power(3,12) returns 2
#closest_power(4,12) returns 2
#closest_power(4,1) returns 0
#Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    i = 0
    while True:
        if abs(base**i - num) <= abs(base**(i+1) - num):
            break
        i += 1
    return i

#Problem 4
#0.0/15.0 points (graded)
#Write a Python function that returns the sum of the pairwise products of listA and listB. You should assume that listA and listB have the same length and are two lists of integer numbers. For example, if listA = [1, 2, 3] and listB = [4, 5, 6], the dot product is 1*4 + 2*5 + 3*6, meaning your function should return: 32
#
#This function takes in two lists of numbers and returns a number.
#
def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    result = 0
    for i in range(len(listB)):
        result += int(listA[i])*int(listB[i])
    return result

        
#  Problem 5
#0.0/20.0 points (graded)
#Write a Python function that returns a list of keys in aDict with the value target. The list of keys you return should be sorted in increasing order. The keys and values in aDict are both integers. (If aDict does not contain the value target, you should return an empty list.)
#
#This function takes in a dictionary and an integer and returns a list.

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here
    result = []
    for key in aDict.keys():
        if aDict[key] == target:
            result.append(key)
    return sorted(result)

#Problem 6
#0.0/20.0 points (graded)
#Implement a function that meets the specifications below.
#
#def max_val(t): 
#    """ t, tuple or list
#        Each element of t is either an int, a tuple, or a list
#        No tuple or list is empty
#        Returns the maximum int in t or (recursively) in an element of t """ 
#    # Your code here
#For example,
#
#max_val((5, (1,2), [[1],[2]])) returns 5.
#max_val((5, (1,2), [[1],[9]])) returns 9.
#Paste your entire function, including the definition, in the box below. Do not leave any debugging print statements.
def max_val(t, lst = []): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """ 
    if isinstance(t, int):
        lst.append(t)
    else:
        for i in t:
            max_val(i, lst)
    return max(lst)         
#incorrect            
    
#Problem 7
#0.0/20.0 points (graded)
#Write a Python function called satisfiesF that has the specification below. Then make the function call run_satisfiesF(L, satisfiesF). Your code should look like:
#
#run_satisfiesF(L, satisfiesF)
#For your own testing of satisfiesF, for example, see the following test function f and test code:
#
def f(s):
    return 'a' in s
#      
#L = ['a', 'b', 'a']
#print satisfiesF(L)
#print L
#Should print:
#
#2
#['a', 'a']
#Paste your entire function satisfiesF, including the definition, in the box below. After you define your function, make a function call to run_satisfiesF(L, satisfiesF). Do not define f or run_satisfiesF. Do not leave any debugging print statements.
#
#For this question, you will not be able to see the test cases we run. This problem will test your ability to come up with your own test cases.
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    lst = []
    for i in L:
        if f(i) == False:
            lst.append(i)
    for j in lst:
        L.remove(j)
    return len(L)

L = ['a', 'b', 'a']
print(satisfiesF(L))
print(L)
            
            
run_satisfiesF(L, satisfiesF)