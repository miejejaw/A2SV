class Solution:
    def reverseString(self, s: List[str]) -> None:
        self.reverse(s,0,len(s)-1)
        return s
    
    def reverse(self, s, beg, end):
        if beg >= end:
            return
        
        self.reverse(s,beg+1,end-1)
        s[end],s[beg] = s[beg],s[end]
        
        