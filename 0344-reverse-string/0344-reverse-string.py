class Solution:
    def reverseString(self, s: List[str]) -> None:
        beg,end = 0,len(s)-1
        while end>beg:
            s[beg],s[end] = s[end],s[beg]
            beg += 1
            end -= 1
        