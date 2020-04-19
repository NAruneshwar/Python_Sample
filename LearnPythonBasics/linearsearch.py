# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 02:08:50 2019

@author: arunn
"""

def search(lis,var):
    for each in lis:
        if(var==each):
             return ("found")



lis = [10,20,30,12,56,87,5,6]
query = 87
result = search(lis,query)
print(result)