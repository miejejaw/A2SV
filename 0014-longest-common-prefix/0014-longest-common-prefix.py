class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i,word = 1,""
        while len(strs[0])>=i:
            for s in strs:
                if strs[0][:i] != s[:i]: 
                    return s[:i-1]
            i += 1
        return strs[0]