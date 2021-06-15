class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxip =  max(piles)
        tempval = maxip
        lessthanlim = True
        while lessthanlim:
            total = 0
            for k in piles:
                total += math.ceil(k//tempval)
            if total<h:
                final = tempval
                tempval-=1
            else:
                lessthanlim = False
        return final
            