class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        ans,m,n = 0,len(grid),len(grid[0])
        def trav(i,j):
            if i<0 or i==m or j<0 or j==n or not grid[i][j]: return
            grid[i][j] = 0
            trav(i+1,j)
            trav(i,j+1)
            trav(i-1,j)
            trav(i,j-1)
            
        for j in range(n): 
            trav(0,j)
            trav(m-1,j)
        for j in range(1,m):
            trav(j,0)
            trav(j,n-1)        
                
        for i in grid:
            ans += i.count(1)
        return ans
        