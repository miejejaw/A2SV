class Solution:
    def numDecodings(self, s: str) -> int:

        self.length = len(s)
        self.dp = {}
        return self.helper(s,0,"11")

    def helper(self, s, ind, ch):
        if ch[0]=="0" or int(ch)>26: return 0
        if ind < self.length:
            if (ind,ch) in self.dp: return self.dp[(ind,ch)]

            self.dp[(ind,ch)] = self.helper(s,ind+1,s[ind])
            if ind+1 < self.length:
                self.dp[(ind,ch)] += self.helper(s,ind+2,s[ind]+s[ind+1])
            return self.dp[(ind,ch)]
        return 1