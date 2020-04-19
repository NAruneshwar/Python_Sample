# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 01:39:00 2019

@author: arunn
"""
fact=1
x=int(input('select the factorial you wana find'))
for k in (range(x,0,-1)):
    fact=fact*k
    
print(fact)