def maxSubArray(nums):
    maximum = nums[0]
    for k in range(len(nums)):
        total = nums[k]
        if nums[k] < total:
            continue
        else:
            total = nums[k]
            if total > maximum:
                maximum = total
            for i in range(k+1, len(nums)):
                if total+nums[i] < 0:
                    break
                else:
                    total += nums[i]
                if total > maximum:
                    maximum = total
    return(maximum)

print(maxSubArray([-2,1]))