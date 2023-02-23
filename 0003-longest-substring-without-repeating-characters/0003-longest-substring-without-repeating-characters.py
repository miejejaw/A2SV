class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = beg = 0
        size = len(s)
        for end in range(size):
            while seen and s[end] in seen:
                seen.remove(s[beg])
                beg += 1
            seen.add(s[end])
            res = max(res,end-beg+1)
        
        return res