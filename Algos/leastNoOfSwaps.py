#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap = 0
    for i in range(0,len(arr)):
        print(arr)
        mini = arr[i]
        valt = i
        for k in range(i+1,len(arr)):
            if(arr[k]<mini):
               
                mini  = arr[k]
                valt = k
        if(mini<arr[i]):
           arr[i],arr[valt]=arr[valt],arr[i]
           swap+=1

    return(swap)
if __name__ == '__main__':
    
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    print(res)  