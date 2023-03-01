class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        res = self.helper(x,abs(n))
        if n < 0:
            return 1/res
        return res
            
    def helper(self, x, n):
        if n == 1:
            return x
        res = self.helper(x,n//2)
        res = res*res
        if n%2 == 1:
            res *= x
        return res
        