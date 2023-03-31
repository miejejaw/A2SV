class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        res = True
        prev = n & 1
        n >>= 1
        while n:
            if n & 1 == prev:
                return False
            prev = n & 1
            n >>= 1
            
        return True
            