class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        lens = len(s)
        for k in range(lens):
            print(s[k])
            if(s[k]=='I'):
                if(k!= lens-1 and s[k+1] in ['V','X','L','C','D','M']):
                    result-=1
                else:
                    result+=1
            if(s[k]=='V'):
                if(k!= lens-1 and s[k+1] in ['X','L','C','D','M']):
                    result-=5
                else:
                    result+=5
            if(s[k]=='X'):
                if(k!= lens-1 and s[k+1] in ['L','C','D','M']):
                    result-=10
                else:
                    result+=10
            if(s[k]=='L'):
                if(k!= lens-1 and s[k+1] in ['C','D','M']):
                    result-=50
                else:
                    result+=50
            if(s[k]=='C'):
                if(k!= lens-1 and s[k+1] in ['D','M']):
                    result-=100
                else:
                    result+=100
            if(s[k]=='D'):
                if(k!= lens-1 and s[k+1]=='M'):
                    result-=500
                else:
                    result+=500
            if(s[k]=='M'):
                result+=1000
            
        
        return result