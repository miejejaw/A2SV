class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return str(self.helper(n,[0],k))
    
    def helper(self, n, s, k):
        if n == 1:
            return s[k-1]
        
        length = len(s)
        temp = [0]*length
        
        for ind in range(length):
            if s[ind] == 0:
                temp[ind] = 1
        
        return self.helper(n-1, s+[1]+temp[::-1], k)