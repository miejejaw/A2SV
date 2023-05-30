class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2: return n
        self.d = {0:0,1:1}
        self.ans = 0
        self.dfs(n)
        if n%2 == 0: n -= 1
        for num in  range(n,2,-1):
            self.dfs(num)
        return self.ans

    def dfs(self,n):
        if n in self.d: return self.d[n]
        self.d[n] = self.dfs(n//2)
        if n%2 == 1:
            self.d[n] += self.dfs(n//2+1)
        self.ans = max(self.ans,self.d[n])
        return self.d[n]