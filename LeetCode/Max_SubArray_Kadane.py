def maxSubArray(nums):
    maxval = nums[0]
    curval = 0
    for k in nums:
        curval += k
        if maxval<curval:
            maxval = curval
        if curval<0:
            curval = 0
    return maxval


print(maxSubArray([-2,-3,-1,-5]))