class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        return(self.ownsearch(nums,target,0,len(nums)-1))
        
        
        
    def ownsearch(self, nums, target, start, end):
        med = math.floor((start+end)/2)
        if start>end:
            return (-1,-1)
        if target == nums[med]:
            origmid = med
            while med !=0 and nums[med]==nums[med-1]:
                med=med-1
            else:
                minele = med
            med = origmid  
            while med !=len(nums)-1 and nums[med]==nums[med+1]:
                med=med+1
            else:
                maxele = med
           
            return (minele,maxele) 
        elif target < nums[med]:
            return self.ownsearch(nums,target,start,med-1)
        elif target > nums[med]:
            return self.ownsearch(nums,target,med+1,end)
