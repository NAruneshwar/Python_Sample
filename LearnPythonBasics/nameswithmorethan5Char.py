# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 19:58:32 2019

@author: arunn
"""
from numpy import *
def names(lis):
    count =0
    for z in lis:
        if(len(z) > 4):
            count+=1
    print(count)    
    
    lis = {}
x = int(input('enter the numer of names you want to enter'))
for k in range(x):
    name=input('enter the name')
    lis['k'] = name
names(lis)