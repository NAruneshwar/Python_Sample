# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 00:39:46 2019

@author: arunn
"""
from time import sleep
from threading import *
class hello(Thread):
    def run(self):
        for i in range(5):
            sleep(.5)
            print("hello")
    
class hi(Thread):
    def run(self):
        for i in range(5):
            sleep(.5)
            print("hi")
        
thread1 = hello()
thread2 = hi()

thread1.start()
sleep(.2)
thread2.start()

thread1.join()
thread2.join()
print('byeeeeeeeeeeeeeee')