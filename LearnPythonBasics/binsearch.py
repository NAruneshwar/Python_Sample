# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 19:30:52 2019

@author: arunn
"""


def binsearch(lis,tar,first,last):
   
    if(first==last):
        return "not possible"        
    k=int((first+last)/2)
   # print(lis[k],tar)
    if(lis[k]==tar):
        return (k)
    elif(lis[k]<tar):
       result = binsearch(lis,tar,k,last)
    elif(lis[k]>tar):
       result= binsearch(lis,tar,first,k)
    
    return(result)


lis = [10,20,30,40,56,87,155,620]
query = 87
result = binsearch(lis,query,0,len(lis)-1)
print("postition is",result+1)