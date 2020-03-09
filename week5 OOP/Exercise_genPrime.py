# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 19:16:21 2020

@author: Effy‘s PC
"""

def genPrimes():
    p1 = 2
    while True:
        for i in range(p1, p1 + 1):#3
            for j in range(2, i):#2
                if i % j == 0:
                    p1 += 1
                    break
            else:
                yield i
                p1 += 1

            
            