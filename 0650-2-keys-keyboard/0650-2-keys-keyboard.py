class Solution:
    def minSteps(self, n: int) -> int:
        
        res = 0
        p = 2
        
        while p*p <= n:
            while n%p == 0:
                res += p
                n //= p
            p += 1
            
        if n > 1:
            res += n
        
        return res
            

            