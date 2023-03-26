class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.length = len(s)
        self.ans = []
        self.helper(s,0,0,[])
        return self.ans
    
    def helper(self,s,ind,count,res):
        
        if ind < self.length and count < 4:
            num = ""
            for i in range(ind,ind+3):
                num += s[i]
                if int(num) > 255:
                    return
                self.helper(s,i+1,count+1,res+[num])
                if num[0] == "0" or i+1 == self.length:
                    return
            return
        
        if count == 4 and ind == self.length:
            self.ans.append(".".join(res))