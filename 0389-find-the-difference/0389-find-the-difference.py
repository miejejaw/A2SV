class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for ch in s:
            t = t.replace(ch,"",1)
        return t