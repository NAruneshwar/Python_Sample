# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 00:55:50 2019

@author: arunn
"""

f = open('sample','r')

f1 = open('test','a')
for words in f:
    f1.write(words)