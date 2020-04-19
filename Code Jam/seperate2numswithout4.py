# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 18:16:21 2019

@author: arunn
"""
def devidetheint(num,i):
    diff = 0
    k = num
    count=1
    if(k%10==4):
        diff = 1
        k=int(k/10)
        count*=10
    while(k>1):
        
        if(k%10==4):
            diff = diff+count
            
        k=int(k/10)
        count*=10
    print("Case #%d: %d %d"%(i+1,diff,num-diff))
   
    return()


count = int(input())

for i in range(count):
    num = int(input())
    devidetheint(num,i)
    