class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.length = len(s)
        self.ans = []
        self.helper(s,0,0,[])
        return self.ans
    
    def helper(self,s,ind,count,res):
        
        if ind < self.length:
            if count == 4:
                return
            
            num = ""
            for i in range(ind,self.length):
                num += s[i]
                if int(num) > 255:
                    return
                self.helper(s,i+1,count+1,res+[num])
                if num[0] == "0":
                    return
                
            return
        
        if count == 4:
            self.ans.append(".".join(res))