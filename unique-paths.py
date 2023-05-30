class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.m,self.n = m,n
        self.d = {(m-1,n-1):1}
        return self.dfs(0,0)

    def dfs(self,row,col):
        if (row,col) in self.d: return self.d[(row,col)]
        res = 0
        x,y = row+1,col
        if self.inbound(x,y):
            res += self.dfs(x,y)
        
        x,y = row,col+1
        if self.inbound(x,y):
            res += self.dfs(x,y)
        
        self.d[(row,col)] = res
        return self.d[(row,col)]

    def inbound(self,row,col):
        return 0<=row<self.m and 0<=col<self.n