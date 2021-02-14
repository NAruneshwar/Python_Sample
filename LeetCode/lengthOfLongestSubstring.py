def lengthOfLongestSubstring(s):
    substring = ""
    max_len = 0
    for k in s:
        if k not in set(substring):
            substring+=k
        elif substring[0] == k:
            substring=substring[1:]+k
        else:
            ind = substring.find(k)
            substring = substring [ind+1:]+k
        if len(substring)>max_len:
            max_len = len(substring)
            
            
    return max_len

print(lengthOfLongestSubstring("ggububgvfk"));