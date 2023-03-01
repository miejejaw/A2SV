class Solution:
    def reverseString(self, s: List[str]) -> None:
        self.reverse(s,0,len(s)-1)
        return s
    
    def reverse(self, s, fr, to):
        if to < 0:
            return
        temp = s[fr]
        self.reverse(s,fr+1,to-1)
        s[to] = temp
        
        