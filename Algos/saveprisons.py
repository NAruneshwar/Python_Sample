# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 22:28:30 2019

@author: arunn
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    print(m%n)
    return((m%n)+s-1)
    
if __name__ == '__main__':
  
    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)
        print(result)
    