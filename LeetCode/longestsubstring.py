    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.checkforpal(s,i,i)
            len2 = self.checkforpal(s,i,i+1)
            length = max(len1,len2)
            if length > end-start:
                start = i-((length-1)//2)
                end = i+(length//2)   

        return s[start:end+1]
    
    def checkforpal(self, s, left, right):
        if s==None or left>right:
            return 0
        while (left >=0 and right <len(s) and s[left]==s[right]):
            left-=1
            right+=1
        return right-left-1