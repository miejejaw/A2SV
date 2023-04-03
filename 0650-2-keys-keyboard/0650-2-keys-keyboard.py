class Solution:
    def minSteps(self, n: int) -> int:
        
        res = []
        p = 2
        
        while p*p <= n:
            while n%p == 0:
                res.append(n)
                n //= p
            p += 1
            
        if n > 1:
            res.append(n)
        res.append(1)
        length = len(res)
        ans = 0
        for ind in range(1,length):
            ans += res[ind-1]//res[ind]
            
        return ans
            

            