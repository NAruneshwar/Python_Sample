# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 00:13:20 2019

@author: arunn
"""

x=int(input('enter the number till where you wana check'))
for m in range(2,x): 
    z=0
    for y in range(1,m):
            
            if m%y==0:
                z+=1
                
    if z<2:
        print('%d is a prime No' % m)
    else:
          print('%d is not a prime No' % m)               