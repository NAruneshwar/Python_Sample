class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        defdic = defaultdict(list)
        for i in strs:
            defdic[''.join(sorted(i))].append(i)
          
        result = []
        for i,j in defdic.items():
            result.append(j)
        
        return result