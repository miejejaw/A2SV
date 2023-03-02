class Solution:
    def findKthBit(self, n: int, k: int, s = [0]) -> str:
        
        if n == 1:
            return str(s[k-1])
        length = len(s)
        temp = [0]*length
        for ind in range(length):
            if s[ind] == 0:
                temp[~ind] = 1
                
        return self.findKthBit(n-1, k, s+[1]+temp)
       

