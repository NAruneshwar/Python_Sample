# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 02:12:34 2019

@author: arunn
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    scores.sort(reverse=True)
    index=0
    rank = {}
    rankvals = {}
    rank[index]=1
    rankvals[1]=scores[0]
    for r in range(1,len(scores)):
        if(scores[r]==scores[r-1]):
            #index+=1
           # rank[index]=rank[index-1]
           pass
           
        else:
            index+=1
            rank[index]=rank[index-1]+1
            rankvals[rank[index]]=scores[r]
    newrank = {}  
    print(rankvals)  
    for new in alice:
        for key,old in rankvals.items():
            if(new<old):
                pass
            elif(new==old):
                newrank[new]=key
                break
            elif(new>old):
                newrank[new]=key
                break
        if(new not in newrank.keys()):
            newrank[new]=max(rankvals)+1
            
    print(newrank)
    return(newrank.values()) 
if __name__ == '__main__':
   
    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

  
