# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 01:31:19 2019

@author: arunn
"""
from threading import *
class first(Thread):
    def run(self,x):
        for m in range(2,x): 
            z=0
            for y in range(1,m):
                    
                    if m%y==0:
                        z+=1
                        
            if z<2:
                print('%d is a prime No' % m)
            else:
                  print('%d is not a prime No' % m)  
class second(Thread):
    def run(self,x):
        for m in range(2,x): 
            z=0
            for y in range(1,m):
                    
                    if m%y==0:
                        z+=1
                        
            if z<2:
                print('%d is a prime No' % m)
            else:
                  print('%d is not a prime No' % m) 
                  
x=int(input('enter the number till where you wana check'))
Case1 = first()
Case2 = second()
Case1.start(x)
Case2.start(x)