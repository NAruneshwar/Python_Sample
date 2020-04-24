import math
class Solution:
    def isHappy(self, n: int) -> bool:
        new_n = 0
        lst = []
        while (n > 0):
            temp = n % 10
            new_n += temp**2
            n = math.floor(n/10)
            if (n==0):
                if(new_n == 1):
                    return True
                n = new_n
                if(n not in lst):
                    lst.append(n)
                    new_n = 0
                else:
                    return False


new1 = Solution()
print(new1.isHappy(19))