# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 17:57:05 2019

@author: arunn
"""
from factorialRec import fact
def sum(*add):
    total=0
    for m in add:
        total += m
        
    print(total)
    
#sum(9,8,9,5,4,6,55,6,4,2,6,65,5,3,3,5,6,6,5,5)
print(fact(5))