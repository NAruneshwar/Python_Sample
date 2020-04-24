def maxSubArray(nums):
    maxval = 0
    curval = 0
    for k in nums:
        curval += k
        if curval<0:
            curval = 0
        if maxval<curval:
            maxval = curval
    return maxval

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))