class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        lis = []
        
        if len(A)!=len(B):
            return False
        else:
            for k in range(len(A)):
                if(A[k]!=B[k]):
                    lis.append(k)
        
        if len(lis) == 0:
            sets = set(A)
            if (len(sets) == len(A)):
                return False
            else:
                return True
        if len(lis) == 2:
            if A[lis[0]]==B[lis[1]]:
                if A[lis[1]]==B[lis[0]]:
                    return True
        
        return False