class Solution:
    def reverseString(self, s: List[str]) -> None:
        self.s = s
        self.reverse(0,len(self.s)-1)
        return self.s
    
    def reverse(self,fr,to):
        if to < 0:
            return
        temp = self.s[fr]
        self.reverse(fr+1,to-1)
        self.s[to] = temp
        
        