# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 12:29:03 2019

@author: arunn
"""
class computer():
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print(self.cpu)
        print(self.ram)
 
comp1 = computer("i7",18) 
comp2 = computer("Core 2 deo", 2)      
comp1.config()
comp2.config()