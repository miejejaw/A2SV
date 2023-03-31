class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        ans = 0
        length = len(words)
        res = self.helper(words)
        
        for ind in range(length):
            _len = len(words[ind])
            for j in range(ind+1,length):
                if self.checker(res[ind],res[j]):
                    ans = max(ans,len(words[j])*_len)
                    
        return ans
                          
    def checker(self,res1,res2):
                          
        while res1 and res2:
            if res1 & 1 == res2 & 1 == 1:
                return False
            res1 >>= 1 
            res2 >>= 1
            
        return True
                          
    def helper(self,words):
        ans = []
        for word in words:
            res = 0
            for ch in word:
                ind = ord(ch) - 97
                res |= 1 << ind
            ans.append(res)
        return ans