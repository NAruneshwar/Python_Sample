class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        for k in range(1,len(height)-1):
            curval = min(max(height[0:k]),max(height[k:]))
            if height[k]<curval:
                total+= curval-height[k] 
        return total