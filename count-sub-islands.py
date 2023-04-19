class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.directions = [(1,0),(0,1),(-1,0),(0,-1)]
        self.rows = len(grid1)
        self.cols = len(grid1[0])
        ans,seen = 0,set()
        for row in range(self.rows):
            for col in range(self.cols):
                if (row,col) not in seen and grid2[row][col]:
                    ans += self.dfs(grid1,grid2,seen,row,col)
                    
        return ans
    
    def inbound(self,row,col):
        return 0<=row<self.rows and 0<=col<self.cols
    
    def dfs(self, grid1, grid2, seen, row, col):
        
        res = True
        seen.add((row,col))
        for x,y in self.directions:
            x += row
            y += col
            if self.inbound(x,y) and grid2[x][y] and (x,y) not in seen:
                res = self.dfs(grid1,grid2,seen,x,y) and res
                  
        return res and grid1[row][col]