class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        self.directions = [(0,1),(1,0),(-1,0),(0,-1)]
        self.rows,self.cols = len(grid),len(grid[0])
        seen,ans = set(),0

        for row in range(self.rows):
            for col in range(self.cols):
                if (row,col) not in seen and grid[row][col]:
                    res = self.dfs(grid,row,col,seen)
                    ans = max(ans,res)
        return ans
    
    def inbound(self,row,col):
        return 0<=row<self.rows and 0<=col<self.cols
    
    def dfs(self,grid,row,col,seen):
        if (row,col) not in seen:
            count = 1
            seen.add((row,col))
            for x,y in self.directions:
                x += row
                y += col
                if self.inbound(x,y) and (x,y) not in seen and grid[x][y]:
                    count += self.dfs(grid,x,y,seen)
                    
            return count
        return 0