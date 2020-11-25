class Solution:
    def reverse(self, x: int) -> int:
        k = x
        result = 0
        
        trig = False
        if(x<0):
            trig = True
            x = -x
        while(x>0):
            k= x%10
            x=int(x/10)
            result = result*10+k
        if result > 2147483647:
            return 0
        if trig == True:
            result = -result
        return result