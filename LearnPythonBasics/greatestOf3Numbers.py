# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 00:25:48 2019

@author: arunn
"""

x = int(input('enter a value'))
y = int(input('enter a value'))
z = int(input('enter a value'))

if(x>y):
    if(x>z):
        print("%d is greatest of %d %d" % (x , y , z))
    elif(z>x):
        print("%d is greatest" % z)
elif(y>x and y>z):
     print("%d is greatest" % y)
else:
      print("%d is greatest" % z)