# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 23:51:10 2019

@author: arunn
"""
z=500
y=[1,2]
print(y[0])
print(y[1])
for x in range(2,z):
    y.append(y[x-1]+y[x-2])
    print(y[x])