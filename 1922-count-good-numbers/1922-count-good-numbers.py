class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9+7
        ans = pow(4,n//2,mod)*pow(5,(n+1)//2,mod)%mod
        return ans
        