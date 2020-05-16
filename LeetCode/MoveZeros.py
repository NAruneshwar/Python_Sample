def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    counter = 0
    for k in range(len(nums)):
        while nums[k] == 0:
            counter += 1
            nums[k:len(nums)-1] = nums[k+1:len(nums)]
            nums[len(nums)-1]=0
            if(counter+k>len(nums)):
                break
    return(nums)


print(moveZeroes([0,1,0,3,12,0]))