# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:46:20 2019

@author: arunn
"""

def sort(arr1):
    for var in range(0,len(arr1),1):
        minval = arr1[var]
        key = var
        for tem in range(var+1,len(arr1),1):
            if(minval > arr1[tem]):
                 minval = arr1[tem]
                 key = tem
        temp = arr1[var]
        arr1[var] = minval
        arr1[key] = temp



arr1 = [20,3,5,7,8,99,88,44,11,23,21,4,5,6,5,88,9,5]
#arr1 = [5,6,8,1]
sort(arr1)
print(arr1)