# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:08:20 2020

@author: Effy‘s PC
6.00.1x, week 1: Python Basics
Problem Set 1
"""
"""
Problem 1
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

Number of vowels: 5
"""
count = 0
for char in s:
    if char == 'a' or char =='e' or char =='i' or char =='o' or char =='u':
        count += 1
        
print('Number of vowels:', count)
#Correct

"""
Problem 2
10.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""
count = 0
for i in range(len(s)-1):
    if s[i:i+3] == 'bob':
        count += 1
print('Number of times bob occurs is:', count)   
#Correct
"""
Problem 3
15.0/15.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.
"""
lst=[]
def check(s):
    result = s[0]#'a'
    lst.append(result)
    for i in range(len(s)-1):#0,1
        if s[i] <= s[i+1]:
            result = result + s[i+1]#'az'
            lst.append(result)
        else:
            return check(s[i+1:])
check(s)
print('Longest substring in alphabetical order is:',max(lst, key=len))
#Correct
