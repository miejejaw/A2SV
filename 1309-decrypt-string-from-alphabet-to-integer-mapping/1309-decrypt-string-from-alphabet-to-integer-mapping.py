class Solution:
    def freqAlphabets(self, s: str) -> str:
        i,ans = len(s)-1,''
        while i >= 0:
            if '#' == s[i]:
                ans = chr(96+int(s[i-2]+s[i-1])) + ans
                i -= 2
            else: 
                ans = chr(96+int(s[i])) + ans
            i -= 1
        return ans