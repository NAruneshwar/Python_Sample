class Solution:
    def intToRoman(self, num: int) -> str:
        convertiondict = { 'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1 }
        total = ''
        for i,j in convertiondict.items():
            re = num//j
            total=total + '' + i*re
            num -= re*j
        
        return total