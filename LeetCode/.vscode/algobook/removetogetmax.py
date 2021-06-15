
def maxnumber(n):
# Function to return the
# largest number possible
    isnegi = False
    if n<0:
        isnegi = True
        n = abs(n)
    i = 1
    result = []
    countn = str(n).count('5')
    while n // i > 0:       
        temp = (n//(i * 10))*i + (n % i)
        i *= 10
        if str(temp).count('5') == countn-1:
            result.append(temp)
    if isnegi:
        result = [i*-1 for i in result]

    return max(result)
   
  
n = -5000
print(maxnumber(n))


# def maxnumber(n):
#     resultantlist = []
#     strn = str(n)
#     for k in range(len(strn)-1,0,-1):
#         if strn[k]=='5':

#             resultantlist.append(int(str(residualval)+str(modval)))
    
    
#     return(max(resultantlist))
  
# n = -5859
# print(maxnumber(n))