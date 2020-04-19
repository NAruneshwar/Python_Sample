# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 22:42:19 2019

@author: arunn
"""



nooftests = int(input())
for k in range(nooftests):
    
    testdata = input().split()
    NoOfPeople = int(testdata[0])
    Maxsize = int(testdata[1])
    matrix = [[0]*Maxsize for i in range(Maxsize)]
    for l in range(NoOfPeople):
        people = input().split()
        XAxis= int(people[0])
        YAxis = int(people[1])
        direction = str(people[2])
        
        
        if(direction=='N'):
            for p in (YAxis+1,Maxsize):
                matrix[XAxis][p] +=1
        elif(people[2]=='S'):
            for p in (YAxis-1,0,-1):
                matrix[XAxis][p] +=1
        elif(people[2]=='E'):
            for p in (XAxis+1):
                matrix[XAxis+1][YAxis] +=1
        elif(people[2]=='W'):
            matrix[XAxis-1][YAxis] +=1
    val = 0
    i = 0 
    j = 0
    for i in range(Maxsize):
        for j in range(Maxsize):
            if(matrix[i][j]>val):
               x= i
               y = j
    print("Case #%d: %d %d"%(k+1,i,j))