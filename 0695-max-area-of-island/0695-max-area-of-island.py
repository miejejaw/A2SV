class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans,row,col,count = 0,len(grid),len(grid[0]),0 
        def helper(i,j):
            if i<0 or i==row or j<0 or j==col or grid[i][j]==0: return 
            nonlocal count
            count += 1
              
            grid[i][j] = 0
            helper(i+1,j)
            helper(i-1,j)
            helper(i,j+1)
            helper(i,j-1)
            
        for i in range(row):
            while 1 in grid[i]:
                helper(i,grid[i].index(1))
                ans = max(ans,count)
                count = 0
        return ans    
    
# 00 10