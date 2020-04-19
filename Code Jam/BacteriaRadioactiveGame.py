# -*- coding: utf-8 -*-
"""
Created on Sat May  4 14:46:32 2019

@author: arunn
"""


def takeinput(rowlen,collen):
    matrix = [[0]*collen for z in range(rowlen)]
    for i in range(rowlen):
        radiodata = input()
        for k in range(collen):
            if(radiodata[k]=='#'):
               matrix[i][k]=1
               
    result = how2win(matrix,rowlen,collen)
    return(result)

def how2win(matrix,rowlen,collen):
    positiveC = 0
    for i in range(rowlen): 
        errflag = 0
        for k in range(collen):        
            if(matrix[i][k]==1):
                errflag =1
               # print(matrix[i][k])
                break
        if(errflag==0):
            positiveC+=collen

#    print(positiveC)
    for i in range(collen): 
        errflag = 0
        for k in range(rowlen):        
            if(matrix[k][i]==1):
                errflag =1
                #print(matrix[k][i])
                break
        if(errflag==0):
            positiveC+=rowlen
 #   print(positiveC)
   # positiveC = rowlen*collen - positiveC
    if((positiveC%2==0 or positiveC<0) and collen!=1):
        return(0)
    else:
        return(positiveC)




nooftests = int(input())
for k in range(nooftests):
    size = input().split()
    result = takeinput(int(size[0]),int(size[1]))
    if(result==1):
        result=2
    print("Case #%d: %d"%(k+1,result))