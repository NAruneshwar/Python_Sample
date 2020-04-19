# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 01:28:26 2019

@author: arunn
"""
k = 1
def fact(n):
    if(n==0 or n==1):
        return 1;
    else:
        return(n*fact(n-1))
    
    

result = fact(5000)
print(result)