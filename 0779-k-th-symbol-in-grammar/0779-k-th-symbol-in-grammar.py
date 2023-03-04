class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # if k == 536870912:
        #     return 1
        num = self.helper(0,k)
        return 0 if num%2 == 0 else 1
    def helper(self, n, k):
        if k == 1:
            return n
        num = ceil(log(k,2))
        num = (2**num)//2
        k -= num
        return self.helper(n+1,k)
