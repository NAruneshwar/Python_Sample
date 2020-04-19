# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:55:22 2019

@author: arunn
"""



def matchable(cskill,kskill,typesofswords,maxfairfight):
    counter =0
    for i in range(0,typesofswords):
        for j in range(typesofswords,i,-1):
            if(abs(max(cskill[i:j])-max(kskill[i:j]))<=maxfairfight):
                counter+=1
    
    return(counter)




nooftests = int(input())
for k in range(nooftests):
    testdata = input().split()
    typesofswords = int(testdata[0])
    maxfairfight = int(testdata[1])
    cskill = list(map(int, input().split())) 
    kskill = list(map(int, input().split())) 
    counter = matchable(cskill,kskill,typesofswords,maxfairfight)
            
    print("Case #%d: %d"%(k+1,counter))