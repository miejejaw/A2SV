class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        res = [i for i in range(1,n+1)]
        k -= 1
        ind = k
        while n>1:
            res.pop(ind)
            n -= 1
            ind = (ind+k)%n
            
        return res[0]
            
            
            
        