# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:58:06 2020

@author: Effy‘s PC
6.00.1x, Week 2: Simple Programs
"""
"""
Exercise: guess my number
 Bookmark this page
Exercise: guess my number
10.0/10.0 points (graded)
ESTIMATED TIME TO COMPLETE: 15 minutes

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer will guess the user's secret number!

Here is a transcript of an example session:

Please think of a number between 0 and 100!
Is your secret number 50?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 75?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 87?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 81?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 84?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. h
Is your secret number 82?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. l
Is your secret number 83?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
Game over. Your secret number was: 83

Note: your program should use input to obtain the user's input! Be sure to handle the case when the user's input is not one of h, l, or c.

When the user enters something invalid, you should print out a message to the user explaining you did not understand their input. Then, you should re-ask the question, and prompt again for input. For example:

Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. y
Sorry, I did not understand your input.
Is your secret number 91?
Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. c
"""
low = 0
high = 100
ans = (low + high) // 2
result = ''
print('Please think of a number between 0 and 100!')
while result != 'c':
    print("Is your secret number ", ans, " ?")
    result = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if result == 'h':
        high = ans
    elif result == 'l':
        low = ans
    elif result != 'l' and result != 'h' and result != 'c':
        print('Sorry, I did not understand your input.')
    ans = (low + high) // 2
print('Game over. Your secret number was:', ans)
#Correct
"""
Exercise: power iter
 Bookmark this page
Exercise: iter power
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 6 minutes

Write an iterative function iterPower(base, exp) that calculates the exponential  baseexp  by simply using successive multiplication. For example, iterPower(base, exp) should compute  baseexp  by multiplying base times itself exp times. Write such a function below.

This function should take in two values - base can be a float or an integer; exp will be an integer  ≥  0. It should return one numerical value. Your code must be iterative - use of the ** operator is not allowed.
"""
def iterPower(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result
#Correct
    
"""
Exercise: power recur
 Bookmark this page
Exercise: power recur
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 7 minutes

In Problem 1, we computed an exponential by iteratively executing successive multiplications. We can use the same idea, but in a recursive function.

Write a function recurPower(base, exp) which computes  baseexp  by recursively calling itself to solve a smaller version of the same problem, and then multiplying the result by base to solve the initial problem.

This function should take in two values - base can be a float or an integer; exp will be an integer  ≥0 . It should return one numerical value. Your code must be recursive - use of the ** operator or looping constructs is not allowed.
"""
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base*recurPower(base, exp-1)
#Correct
"""
Exercise: gcd iter
 Bookmark this page
Exercise: gcd iter
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 5 minutes

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.
"""
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a == 1 or b == 1:
        return 1
    test = a
    while a%test > 0 or b%test > 0:
        test -= 1
        if test == 1:
            break
    return test
#Correct
    
"""
Exercise: gcd recur
 Bookmark this page
Exercise: gcd recur
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 6 minutes

The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

gcd(2, 12) = 2

gcd(6, 12) = 6

gcd(9, 12) = 3

gcd(17, 12) = 1

A clever mathematical trick (due to Euclid) makes it easy to find greatest common divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a

Otherwise, gcd(a, b) is the same as gcd(b, a % b)

See this website for an example of Euclid's algorithm being used to find the gcd.

Write a function gcdRecur(a, b) that implements this idea recursively. This function takes in two positive integers and returns one integer.
"""
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    
    else:
        return gcdRecur(b, a%b)
#Correct    
        
"""
Exercise: is in
 Bookmark this page
Exercise: is in
5.0/5.0 points (graded)
ESTIMATED TIME TO COMPLETE: 18 minutes

We can use the idea of bisection search to determine if a character is in a string, so long as the string is sorted in alphabetical order.

First, test the middle character of a string against the character you're looking for (the "test character"). If they are the same, we are done - we've found the character we're looking for!

If they're not the same, check if the test character is "smaller" than the middle character. If so, we need only consider the lower half of the string; otherwise, we only consider the upper half of the string. (Note that you can compare characters using Python's < function.)

Implement the function isIn(char, aStr) which implements the above idea recursively to test if char is in aStr. char will be a single character and aStr will be a string that is in alphabetical order. The function should return a boolean value.

As you design the function, think very carefully about what the base cases should be.
"""
def isIn(char, aStr):
    if aStr == '':
        return False
    elif len(aStr) == 1:
        return char == aStr[0]  
    middle_index = len(aStr)//2
    middle = aStr[middle_index]
    if char == middle:
        return True
    elif char < middle:
        return isIn(char, aStr[:middle_index])
    else:
        return isIn(char, aStr[middle_index+1:])
#Correct 

