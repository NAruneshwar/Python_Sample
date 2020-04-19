# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 00:29:07 2019

@author: arunn
"""

def Sort(nums):
    for d in range(len(nums)-1,0,-1):
        for k in range(0,d,1):
            if(nums[k]>nums[k+1]):
                temp = nums[k]
                nums[k] = nums [k+1]
                nums[k+1]= temp
    
    
    
    
arr1 = [20,3,5,7,8,99,88,44,11,23,21,4,5,6,5,88,9,5]
Sort(arr1)
print(arr1)