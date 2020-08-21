class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even = []
        odd = []
        for k in A:
            if k%2==0:
                even.append(k)
            else:
                odd.append(k)
        
        return(even+odd)