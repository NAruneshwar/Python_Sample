# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 22:21:13 2019

@author: arunn
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    count=0
    index = 0
    if (i<j):
        index=1
        j+=1
    if (i>j):
        index=-1
        i+=1
    for l in range(i,j,index):
        #print(l)
        m=l
        #print(l)
        devisor=1
        totallen = int(len(str(l)))
        #print(totallen)
        for iterator in range (totallen-1):
            devisor = devisor *10
        
        #print("temp"+temp)
        while(devisor>=10):
            temp = l%devisor
            l=int(l/devisor)
            #print(l)
            l= l + devisor*temp
            devisor = devisor/10
        
        #print(l)
        if((abs(m-l)%k)==0):
            count = count+1
    
    return(count)

if __name__ == '__main__':

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)
    print(result)