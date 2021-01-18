def twoSum(nums, target):
    lis = sorted(nums)
    k,l = 0,len(lis)
    l=l-1
    val1, val2 = 0,0
    while(k<len(lis) and l>0): 
        if lis[k]+lis[l]==target:
            val1 = lis[l]
            val2 = lis[k]
        elif lis[k]+lis[l]<target:
            k+=1
        elif lis[k]+lis[l]>target:
            l-=1
        print(val1,val2)


twoSum([2,4,1,3],4)