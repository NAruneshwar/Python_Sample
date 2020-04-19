# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:10:59 2019

@author: arunn
"""

nooftests = int(input())
for k in range(nooftests):
    size = int(input())
    lis = {}
    for m in range(size):
        lis[m]=input()
    for k in range(len(lis)):
        lis[k][len(k)%k]            