# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 01:35:46 2019

@author: arunn
"""
class student:
    def __init__(self,name):
        self.name = name
        self.lap= self.laptop
        
    class laptop:
        config = 'I7'
    
stud1 = student('arun')
stud2 = student.laptop
print(stud1.lap.config)
print(stud2.config)